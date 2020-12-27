# OrganiApp

Key Words: Python Django uWSGI RaspberryPi4 Docker DockerCompose NGINX

OrganiApp is a Django-uWSGI App, deployed on my RaspberryPi 4 with Docker, Docker-compose and nginx.

OrganiApp is a "Family Shared List". Lists are shared through a family server (like RaspberryPi or example). Each device can acces to the lists modify them, add or remove.
For each list, items can be added or removed.

I use also Font-Awesome-4 for CSS Icons

## 12 Factor App Manifesto

I personnaly think following the [12 factor app methodology](https://12factor.net) is a good way of putting an app on production mode. I tkink Docker system is helping in the 12 factor app manifesto.
This is why I propose an easy "Install and Run" solution:

### Installation

You will need Docker and Docker-Compose installed

ON RASPBERRY PI 4, please follow these commands:
```bash
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi       -> (REBOOT or run next command with sudo)
docker run hello-world
sudo apt-get install -y libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get remove python-configparser
sudo pip3 -v install docker-compose
```

DON'T FORGET to:
- add the Host IP-Adress in "docker-compose-deploy.yml" (I made a #comment)
- change the SECRET_KEY in "docker-compose-deploy.yml" (I made a #comment)
- change the ADMIN PATH in /Organi/Organi/urls.py (I made a #comment)


### Run Server

Please cd in current directory
```bash
cd /Organi/
```

-> Run on Dev-mod   The server will be set on 8000
```bash
Docker-compose up
```

-> Run on Prod-mod (first time)     The server will be set on 8080
```bash
cd proxy
docker build .
cd ..
docker-compose -f docker-compose-deploy.yml up –build
```

-> Run on Prod-mod (no need to rebuild)
```bash
docker-compose -f docker-compose-deploy.yml up
```

Then go on localhost:8000 or :8080. The "welcome web-page" should appear.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

To contribute to OrganiApp, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contact

If you want to contact me you can reach me at romain.ledru2@gmail.com

### Next Steps!

Well, if you are still reading, that maybe means that you are interested in the project.

If you want to work together, share our knowledges, ideas, or build something together: 
I would be glad to find a developer-partner.


As always ...
Feel free to propose new ideas! :smiley: