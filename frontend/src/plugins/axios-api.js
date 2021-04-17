import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'https://bullet.srvz-webapp.he-arc.ch/backend/',
    timeout: 5000,
})

export { getAPI };