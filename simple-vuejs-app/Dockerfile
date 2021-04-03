FROM node:12.20.1-alpine as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json ./
RUN npm i --silent
RUN npm install react-scripts@3.4.1 -g --silent
COPY . ./
# ENV REACT_APP_HOST_IP_ADDRESS $API_URL
RUN npm run build

# production environment
FROM nginx:1.13
RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/nginx/nginx.conf /etc/nginx/conf.d/default.conf:ro
COPY --from=build /app/dist /usr/share/nginx/html

# to test image over local quickly, just comment above part, uncomment this below part, hit npm run build
# once build is successful, run docker compose file


# FROM nginx:1.13
# RUN  apt-get update \
#   && apt-get install -y wget \
#   && rm -rf /var/lib/apt/lists/*
# RUN  wget https://github.com/jgm/pandoc/releases/download/1.15.1/pandoc-1.15.1-1-amd64.deb
# RUN  dpkg -i pandoc-1.15.1-1-amd64.deb
# RUN rm -rf /usr/share/nginx/html/*
# COPY /nginx/nginx.conf /etc/nginx/conf.d
# COPY  /dist /usr/share/nginx/html
# FROM node:lts-alpine

# # install simple http server for serving static content
# RUN npm install -g http-server

# # make the 'app' folder the current working directory
# WORKDIR /app

# # copy both 'package.json' and 'package-lock.json' (if available)
# COPY package*.json ./

# # install project dependencies
# RUN npm install

# # copy project files and folders to the current working directory (i.e. 'app' folder)
# COPY . .

# # build app for production with minificationdocker
# RUN npm run build

# EXPOSE 8080
# CMD [ "http-server", "dist" ]