import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../plugins/axios-api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    username: null,
    configs: [],
    platforms: [],
    ammos: [],
    cannons: [],    
    simulatorData: [],
  },
  mutations: {
    updateStorage(state, { access, refresh, username }) {
      state.accessToken = access
      state.refreshToken = refresh
      state.username = username
      localStorage.setItem('accessToken', access);
      localStorage.setItem('username', username)
    },
    destroyToken(state) {
      state.accessToken = null
      state.refreshToken = null
      localStorage.removeItem('accessToken')
      localStorage.removeItem('username')
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
    updateSimulator(state, data) {
      state.simulatorData = data;
    }
  },
  getters: {
    loggedIn(state) {
      if (localStorage.getItem('accessToken') != null) {
        state.accessToken = localStorage.getItem('accessToken');
        state.username = localStorage.getItem('username');
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
    async postConfig({ state, dispatch }, newConfig) {
      try {
        //console.log(newConfig);
        const response = await getAPI.post('/api/configs/', newConfig);
        const newConfigId = response.data.id;

        const myConfigs = state.configs.map(config => config.id);
        myConfigs.push(newConfigId);
        console.log(myConfigs);
        await getAPI.patch(`/api/users/${state.username}/`, { "config": myConfigs }, {
          headers: { Authorization: `Bearer ${state.accessToken}` }
        })

        // Then, reload configs
        dispatch('fetchConfigs');
      } catch (error) {
        console.log(error);
      }
    },
    async fetchConfigs({ commit, state }) {
      try {
        const responseUserConfig = await getAPI.get(`/api/users/${state.username}/`, {
          headers: { Authorization: `Bearer ${state.accessToken}` }
        });
        const userConfigs = responseUserConfig.data.config;

        const response = await getAPI.get('/api/configs/');
        const configs = response.data;
        const myConfigs = configs.filter(config => userConfigs.includes(config.id));
        commit('updateConfigs', myConfigs);
      } catch (error) {
        console.log(error);
      }
    },
    async patchConfig({ dispatch }, payload) {
      try {
        //console.log(payload);
        await getAPI.patch('/api/configs/' + payload["id"] + '/', payload["patchedConfig"]);

        // Then, reload configs
        dispatch('fetchConfigs');
      } catch (error) {
        console.log(error.response.data);
      }
    },
    async deleteConfig({ dispatch }, configId) {
      try {
        await getAPI.delete('/api/configs/' + configId);

        // Then, reload configs
        dispatch('fetchConfigs');
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
    async fetchSimulatorData({ commit, state }) {
      try {
        const response = await getAPI.get(`/api/users/${state.username}/`);
        commit('updateSimulator', response.data);
      } catch (error) {
        console.log(error);
      }
    },
  },
  modules: {
  }
})