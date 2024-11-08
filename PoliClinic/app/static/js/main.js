const serverUrl = "http://127.0.0.1:8000/";

// Функция для загрузки докторов и обновления списка
function loadDoctors() {
    fetch(`${serverUrl}api/v1/doctors/`)
        .then(response => response.json())
        .then(doctors => {
            const doctorSelect = document.getElementById('doctor');
            doctorSelect.innerHTML = '<option value="" disabled selected>Выберите врача</option>'; // очищаем старые данные

            // Заполняем список врачей
            doctors.forEach(doctor => {
                const option = document.createElement('option');
                option.value = doctor.user.id; // здесь устанавливаем id доктора как value
                const doctorName = `${doctor.user.first_name} ${doctor.user.last_name}`; // Формируем имя врача
                const specialization = doctor.specialization.specialization;

                option.textContent = `${doctorName} (${specialization})`; // Формат отображения
                doctorSelect.appendChild(option);
            });
        })
        .catch(error => {
            console.error("Ошибка при загрузке списка докторов:", error);
            const doctorSelect = document.getElementById('doctor');
            doctorSelect.innerHTML = '<option value="" disabled>Не удалось загрузить врачей</option>';
        });
}

window.addEventListener('DOMContentLoaded', loadDoctors);


function getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith(name + '=')) {
            return decodeURIComponent(cookie.substring(name.length + 1));
        }
    }
    return null;
}


document.getElementById('recordForm').addEventListener('submit', function(event) {
    event.preventDefault(); // предотвращаем стандартное отправление формы

    const formData = new FormData(this); // получаем все данные формы

    // Собираем данные в объект, включая ID доктора, выбранного пользователем
    const recordData = {
        name_records: formData.get('name_records'),  // Название записи
        doctor: formData.get('doctor'),  // ID выбранного врача
        date_record: formData.get('date'),  // Дата записи
        date_time: formData.get('time'),  // Время записи
        date_create: new Date().toISOString()  // Текущая дата в формате ISO
    };
    console.log(recordData)
    // Отправка данных на сервер через POST запрос
    fetch('http://127.0.0.1:8000/api/v1/records/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),  // CSRF токен для защиты
        },
        body: JSON.stringify(recordData)  // преобразуем данные в строку JSON
    })
    .then(response => response.json())
    .then(data => {
        console.log("Запись создана:", data);
        // Уведомление или другое действие после успешной записи
    })
    .catch(error => {
        console.error("Ошибка при создании записи:", error);
    });
});

