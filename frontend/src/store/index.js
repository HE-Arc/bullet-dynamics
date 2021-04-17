import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../plugins/axios-api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    configs: [],
    platforms: [],
    ammos: [],
    cannons: [],
    username: null,
  },
  mutations: {
    updateStorage (state, { access, refresh, username }) {
      state.accessToken = access
      state.refreshToken = refresh
      state.username = username
      localStorage.setItem('accessToken', access);
    },
    destroyToken(state) {
      state.accessToken = null
      state.refreshToken = null
      localStorage.removeItem('accessToken')
    },
    updateConfigPlatform(state, { configId, id }) {
      state.configs.find(config => config.id == configId).platform = id;
    },
    updateConfigAmmo(state, { configId, id }) {
      state.configs.find(config => config.id == configId).ammo = id;
    },
    updateConfigCannon(state, { configId, id }) {
      state.configs.find(config => config.id == configId).cannon = id;
    },
    updateConfigs(state, data) {
      state.configs = data;
    },
    updateCannons(state, data) {
      state.cannons = data;
    },
    updatePlatforms(state, data) {
      state.platforms = data;
    },
    updateAmmos(state, data) {
      state.ammos = data;
    },
  },
  getters: {
    loggedIn(state) {
      if (localStorage.getItem('accessToken') != null) {
        state.accessToken = localStorage.getItem('accessToken');
      }
      return state.accessToken != null;
    }
  },
  actions: {
    userLogout(context) {
      if (context.getters.loggedIn) {
        context.commit('destroyToken')
      }
    },
    userLogin (context, usercredentials) {
      let username = usercredentials.username;
      return new Promise((resolve, reject) => {
        getAPI.post('/api-token/', {
          username: username,
          password: usercredentials.password
        })
          .then(response => {
            context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh, username }) 
            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    async fetchConfigs({ commit }) {
      try {
        const response = await getAPI.get('/api/configs/');
        commit('updateConfigs', response.data);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchPlatforms({ commit }) {
      try {
        const response = await getAPI.get('/api/platforms/');
        commit('updatePlatforms', response.data);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchAmmos({ commit }) {
      try {
        const response = await getAPI.get('/api/ammos/');
        commit('updateAmmos', response.data);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchCannons({ commit }) {
      try {
        const response = await getAPI.get('/api/cannons/');
        commit('updateCannons', response.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
  modules: {
  }
})