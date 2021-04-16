import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../plugins/axios-api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    APIData: '',
    configs: null,
    platforms: null,
    ammunitions: null,
    cannons: null,
  },
  mutations: {
    updateStorage(state, { access, refresh }) {
      state.accessToken = access
      state.refreshToken = refresh
      localStorage.setItem('accessToken', access);
    },
    destroyToken(state) {
      state.accessToken = null
      state.refreshToken = null
      localStorage.removeItem('accessToken')
    },
    updateConfigPlatform(state, { configId, id }) {
      state.configs.forEach(function (part, index) {
        if (state.configs[index].id == configId)
          state.configs[index].plateform_id = id;
      });
    },
    updateConfigAmmunition(state, { configId, id }) {
      state.configs.forEach(function (part, index) {
        if (state.configs[index].id == configId)
          state.configs[index].munition_id = id;
      });
    },
    updateConfigCannon(state, { configId, id }) {
      state.configs.forEach(function (part, index) {
        if (state.configs[index].id == configId)
          state.configs[index].cannon_id = id;
      });
    }
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
    userLogin(context, usercredentials) {
      return new Promise((resolve, reject) => {
        getAPI.post('/api-token/', {
          username: usercredentials.username,
          password: usercredentials.password
        })
          .then(response => {
            context.commit('updateStorage', { access: response.data.access, refresh: response.data.refresh })
            resolve()
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    async fetchConfigs() {
      try {
        const response = await getAPI.get('/user/0/configs');
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchPlatforms() {
      try {
        const response = await getAPI.get('/platforms');
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchAmmunitions() {
      try {
        const response = await getAPI.get('/ammunitions');
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchCannons() {
      try {
        const response = await getAPI.get('/cannons');
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
  },
  modules: {
  }
})
