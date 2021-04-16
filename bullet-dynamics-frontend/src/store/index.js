import Vue from 'vue'
import Vuex from 'vuex'
import { getAPI } from '../plugins/axios-api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    APIData: '',
    configs: [{id:1, name:"conf test 1", ammo_id:1, platform_id:2, cannon_id:3}, {id:2, name:"conf test 2", ammo_id:2, platform_id:2, cannon_id:3}],
    platforms: [],
    ammos: [],
    cannons: []
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
          state.configs[index].platform_id = id;
      });
    },
    updateConfigAmmo(state, { configId, id }) {
      state.configs.forEach(function (part, index) {
        if (state.configs[index].id == configId)
          state.configs[index].ammo_id = id;
      });
    },
    updateConfigCannon(state, { configId, id }) {
      state.configs.forEach(function (part, index) {
        if (state.configs[index].id == configId)
          state.configs[index].cannon_id = id;
      });
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
    async fetchConfigs({commit}) {
      try {
        const response = await getAPI.get('/api/configs/');
        commit('updatePlatforms', response.data);
        //console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchPlatforms({commit}) {
      try {
        const response = await getAPI.get('/api/platforms/');
        commit('updatePlatforms', response.data);
        //console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchAmmos({commit}) {
      try {
        const response = await getAPI.get('/api/ammos/');
        commit('updateAmmos', response.data);
        //console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchCannons({commit}) {
      try {
        const response = await getAPI.get('/api/cannons/');
        commit('updateCannons', response.data);
        //console.log(state.cannons);
      } catch (error) {
        console.log(error);
      }
    },
  },
  modules: {
  }
})
