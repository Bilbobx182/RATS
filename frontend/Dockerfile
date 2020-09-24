# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
FROM tiangolo/node-frontend:10 as build-stage
WORKDIR /app
COPY package*.json /app/
RUN npm install
COPY ./ /app/
RUN npm run build

FROM nginx:1.15-alpine
COPY --from=build-stage /app/build/ /usr/share/nginx/html
# Copy the default nginx.conf provided by tiangolo/node-frontend

COPY --from=build-stage /app/ssl/ /etc/nginx/ciaranssl/
COPY --from=build-stage /app/ssl/onuallaic.dev.key /etc/nginx/ciaranssl/onuallaic.dev.key

COPY --from=build-stage /app/default.conf /etc/nginx/conf.d/default.conf