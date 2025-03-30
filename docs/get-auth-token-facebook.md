
## 2. Получение OAuth-токена от Facebook

### 2.1 Создание приложения в Facebook Developer
1. Перейдите в [Facebook for Developers](https://developers.facebook.com/).
2. Войдите в аккаунт и нажмите **"Создать приложение"**.
3. Выберите **"Consumer"** и нажмите **"Продолжить"**.
4. Введите имя приложения, email и выберите бизнес-аккаунт (если есть).
5. Перейдите в **Настройки → Основные** и сохраните **App ID** и **App Secret**.
6. В разделе **Facebook Login** добавьте **Valid OAuth Redirect URIs** (например, `https://yourapp.com/auth/facebook/callback`).

### 2.2 Получение Access Token от Facebook

#### 2.2.1 Получение кода авторизации
Направьте пользователя на URL Facebook OAuth:
```plaintext
https://www.facebook.com/v12.0/dialog/oauth?
  client_id=YOUR_APP_ID&
  redirect_uri=YOUR_REDIRECT_URI&
  scope=email,public_profile
```
После успешной авторизации Facebook перенаправит пользователя на `YOUR_REDIRECT_URI` с `code`.

#### 2.2.2 Обмен кода на Access Token
Отправьте `GET`-запрос:
```bash
curl -X GET "https://graph.facebook.com/v12.0/oauth/access_token?
  client_id=YOUR_APP_ID&
  client_secret=YOUR_APP_SECRET&
  redirect_uri=YOUR_REDIRECT_URI&
  code=AUTHORIZATION_CODE"
```
Ответ:
```json
{
  "access_token": "EAAGm0PX4ZCpsBA...",
  "token_type": "bearer",
  "expires_in": 5184000
}
```

### 2.3 Получение информации о пользователе
Используйте `access_token` для запроса данных:
```bash
curl -X GET "https://graph.facebook.com/me?fields=id,name,email,picture&access_token=ACCESS_TOKEN"
```
Ответ:
```json
{
  "id": "1234567890123456",
  "name": "John Doe",
  "email": "example@gmail.com",
  "picture": {
    "data": {
      "height": 50,
      "width": 50,
      "url": "https://platform-lookaside.fbsbx.com/..."
    }
  }
}
```

---

Теперь у вас есть `access_token` для Google и Facebook, который можно использовать в вашем проекте для аутентификации пользователей. 🚀

