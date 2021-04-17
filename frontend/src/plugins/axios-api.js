import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'https://bullet.srvz-webapp.he-arc.ch/backend/', // need to change it later (use a env) (but not enough time to do so)
    //baseURL: 'http://localhost:8000/backend/',
    timeout: 5000,
})

export { getAPI };