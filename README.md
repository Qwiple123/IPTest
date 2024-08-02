<body>
    <div class="container">
        <h1>Dockerized FastAPI and Aiogram Telegram Bot</h1>
        <p>Этот проект представляет собой комплексное решение для создания и управления сообщениями с использованием FastAPI, MongoDB, Nginx, Redis и Aiogram. Включает в себя:</p>
        <ul>
            <li>FastAPI приложение с несколькими API-эндпоинтами.</li>
            <li>Телеграм-бот, созданный с использованием библиотеки Aiogram, для взаимодействия с API.</li>
            <li>Кэширование сообщений с использованием Redis.</li>
            <li>Пагинация сообщений.</li>
            <li>Подробное описание развертывания и настройки.</li>
        </ul>

        <h2>Структура проекта</h2>

        <h3>FastAPI приложение</h3>
        <ul>
            <li><strong>GET</strong> <code>/api/v1/messages/</code> - Получить список всех сообщений.</li>
            <li><strong>POST</strong> <code>/api/v1/message/</code> - Создать новое сообщение.</li>
            <li><strong>GET</strong> <code>/api/v1/users/</code> - Получить пользователя по <code>user_id</code>.</li>
            <li><strong>POST</strong> <code>/api/v1/users/</code> - Создать пользователя.</li>
            <li><strong>GET</strong> <code>/api/v1/messages/count</code> - Получить количество сообщений в базе данных.</li>
        </ul>

        <h3>Телеграм-бот</h3>
        <ul>
            <li>Использует Aiogram для взаимодействия с пользователями через Telegram.</li>
            <li>Отображает сообщения и позволяет пользователям создавать новые сообщения.</li>
        </ul>

        <h3>Redis</h3>
        <ul>
            <li>Используется для кэширования сообщений, кэш очищается при создании нового сообщения.</li>
        </ul>

        <h3>Nginx</h3>
        <ul>
            <li>Веб-сервер, который проксирует запросы к FastAPI приложению.</li>
        </ul>

        <h3>MongoDB</h3>
        <ul>
            <li>База данных для хранения сообщений.</li>
        </ul>

        <h2>Требования</h2>
        <ul>
            <li>Docker</li>
            <li>Docker Compose</li>
        </ul>

        <h2>Запуск проекта</h2>
        <ol>
            <li><strong>Клонируйте репозиторий:</strong></li>
            <pre><code>git clone https://github.com/<Ваш юзернейм>/IPTest.git
cd IPTest</code></pre>
            <li><strong>Запустите контейнеры:</strong></li>
            <pre><code>docker-compose up --build</code></pre>
            <p>Это развернет FastAPI приложение, Nginx, MongoDB, Redis и Aiogram бота.</p>
        </ol>

        <h2>Эндпоинты FastAPI</h2>
        <ul>
            <li><strong>GET</strong> <code>/api/v1/messages/</code> - Получить список всех сообщений.
                <p><strong>Пример ответа:</strong></p>
                <pre><code>[
    {
        "id": "message_id",
        "user_id": 12345,
        "content": "Your message content",
        "created_at": "2024-08-02T12:34:56"
    }
]</code></pre>
            </li>
            <li><strong>POST</strong> <code>/api/v1/message/</code> - Создать новое сообщение.
                <p><strong>Пример запроса:</strong></p>
                <pre><code>{
    "user_id": 12345,
    "content": "Your message content"
}</code></pre>
            </li>
            <li><strong>GET</strong> <code>/api/v1/users/</code> - Получить пользователя по <code>user_id</code>.
                <p><strong>Пример ответа:</strong></p>
                <pre><code>{
    "user_id": 12345,
    "nick_name": "YourNickname"
}</code></pre>
            </li>
            <li><strong>POST</strong> <code>/api/v1/users/</code> - Создать пользователя.
                <p><strong>Пример запроса:</strong></p>
                <pre><code>{
    "user_id": 12345,
    "nick_name": "YourNickname"
}</code></pre>
            </li>
            <li><strong>GET</strong> <code>/api/v1/messages/count</code> - Получить количество сообщений в базе данных.
                <p><strong>Пример ответа:</strong></p>
                <pre><code>{
    "count": 42
}</code></pre>
            </li>
        </ul>

        <h2>Телеграм-бот</h2>
        <ul>
            <li><strong>Команда <code>/start</code></strong> - Запускает бота и показывает приветственное сообщение.</li>
            <li><strong>Инлайн кнопка "Написать сообщение"</strong> - Позволяет отправить новое сообщение.</li>
            <li><strong>Инлайн кнопка "Посмотреть сообщения"</strong> - Показывает список сообщений с пагинацией.</li>
        </ul>

        <h2>Лицензия</h2>
        <p>Этот проект лицензирован на условиях <a href="LICENSE">MIT License</a>.</p>

        <h2>Контактная информация</h2>
        <p>Если у вас есть вопросы, вы можете связаться со мной по <a href="mailto:email@example.com">email@example.com</a>.</p>
    </div>
</body>