import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../plugins/axios-api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    APIData: '',
    configs: {
      1: { id: 1, name: "conf test 1", ammo_id: 1, platform_id: 1, cannon_id: 1 },
      2: { id: 2, name: "conf test 2", ammo_id: 2, platform_id: 2, cannon_id: 2 },
    },
    platforms: {
      1: { "id": 1, "name": "AR-15", "weight": 3, "price": 1500, "length": 0.83, "standard_cannon_length": 0.406 },
      2: { "id": 2, "name": "AK-M", "weight": 3.5, "price": 500, "length": 0.88, "standard_cannon_length": 0.37 },
    },
    ammos: {
      1: { "id": 1, "name": "5.56 NATO", "weight": 0.37, "price": 0.5, "bullet_weight": 0.004, "cx": 0.37 },
      2: { "id": 2, "name": "7.62 NATO", "weight": 0.75, "price": 1.2, "bullet_weight": 0.010, "cx": 0.475 },
    },
    cannons: {
      1: { "id": 1, "name": "10.5\" light", "weight": 0.50, "price": 200, "length": 0.267 },
      2: { "id": 2, "name": "14\" M4 milspec", "weight": 0.70, "price": 150, "length": 0.37 },
    },
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
      state.configs[configId].platform_id = id;
    },
    updateConfigAmmo(state, { configId, id }) {
      state.configs[configId].ammo_id = id;
    },
    updateConfigCannon(state, { configId, id }) {
      state.configs[configId].cannon_id = id;
    },
    updatConfigs(state, data) {
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
    async fetchConfigs({ commit }) {
      try {
        const response = await getAPI.get('/api/configs/');
        commit('updatePlatforms', response.data);
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