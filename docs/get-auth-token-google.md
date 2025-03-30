# Получение OAuth-токенов от Google и Facebook

## 1. Получение OAuth-токена от Google

### 1.1 Создание проекта в Google Cloud Console
1. Перейдите в [Google Cloud Console](https://console.cloud.google.com/).
2. Создайте новый проект (или используйте существующий).
3. В левом меню выберите **"API и сервисы" → "Учетные данные"**.
4. Нажмите **"Создать учетные данные"** и выберите **OAuth 2.0 Client ID**.
5. Если требуется, настройте **экран согласия OAuth**:
   - Выберите **внешний** (если пользователи вне вашей организации будут использовать OAuth).
   - Заполните основные данные (имя приложения, контактный email).
   - Укажите **разрешенные URL-адреса** и **области доступа (scopes)**.
   - Сохраните настройки.
6. Выберите **тип приложения** (например, Web application).
7. В разделе **Authorised redirect URIs** укажите URL вашего сервера (например, `https://yourapp.com/auth/google/callback`).
8. Нажмите **Создать** и сохраните **Client ID** и **Client Secret**.

### 1.2 Получение Access Token от Google

Отправьте HTTP-запрос на Google OAuth API для получения токена:

#### 1.2.1 Получение кода авторизации
Направьте пользователя на следующий URL:
```plaintext
https://accounts.google.com/o/oauth2/auth?
  client_id=YOUR_CLIENT_ID&
  redirect_uri=YOUR_REDIRECT_URI&
  response_type=code&
  scope=email profile
```
После успешной авторизации Google перенаправит пользователя на `YOUR_REDIRECT_URI` с параметром `code`.

#### 1.2.2 Обмен кода на Access Token
Отправьте `POST`-запрос на Google OAuth API:
```bash
curl -X POST https://oauth2.googleapis.com/token \
  -d client_id=YOUR_CLIENT_ID \
  -d client_secret=YOUR_CLIENT_SECRET \
  -d redirect_uri=YOUR_REDIRECT_URI \
  -d grant_type=authorization_code \
  -d code=AUTHORIZATION_CODE
```
Ответ:
```json
{
  "access_token": "ya29.A0AfH6SM...",
  "expires_in": 3600,
  "refresh_token": "1//0g...",
  "scope": "email profile",
  "token_type": "Bearer"
}
```

### 1.3 Получение информации о пользователе
Используйте `access_token` для запроса данных:
```bash
curl -H "Authorization: Bearer ACCESS_TOKEN" https://www.googleapis.com/oauth2/v1/userinfo
```
Ответ:
```json
{
  "id": "102851062426860590103",
  "email": "example@gmail.com",
  "verified_email": true,
  "name": "John Doe",
  "given_name": "John",
  "family_name": "Doe",
  "picture": "https://lh3.googleusercontent.com/..."
}
```

---
