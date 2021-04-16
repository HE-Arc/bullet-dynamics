import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    configs: [
      { id: 0, name: "Config alpha", cannon_id: 0, munition_id: 0, plateform_id: 0 },
      { id: 1, name: "Config beta", cannon_id: 0, munition_id: 0, plateform_id: 0 },
    ],
    platforms: [
      { id: 0, desc: "Platform alpha", weight: 2, price: 500, length: 80, standard_cannon_length: 20 },
      { id: 1, desc: "Platform beta", weight: 0, price: 0, length: 0, standard_cannon_length: 0 },
      { id: 2, desc: "Platform 3", weight: 0, price: 0, length: 0, standard_cannon_length: 0 },
      { id: 3, desc: "Platform 4", weight: 0, price: 0, length: 0, standard_cannon_length: 0 },
      { id: 4, desc: "Platform 5", weight: 0, price: 0, length: 0, standard_cannon_length: 0 },
      { id: 5, desc: "Platform 6", weight: 0, price: 0, length: 0, standard_cannon_length: 0 },
      { id: 6, desc: "Platform 7", weight: 0, price: 0, length: 0, standard_cannon_length: 0 },
    ],
    ammunitions: [
      { id: 0, desc: "Ammunition alpha", weight: 0.2, price: 40, bullet_weight: 0, cx: 0 },
      { id: 1, desc: "Ammunition beta", weight: 0, price: 0, bullet_weight: 0, cx: 0 },
    ],
    cannons: [
      { id: 0, desc: "Cannon alpha", weight: 1, price: 100, length: 15 },
      { id: 1, desc: "Cannon beta", weight: 0, price: 0, length: 0 },
    ],
  },
  mutations: {
    updateConfigPlatform(state, payload) {
      state.configs.forEach(function (part, index) {
        if (state.configs[index].id == payload.configId)
          state.configs[index].plateform_id = payload.id;
      });
    },
    updateConfigAmmunition(state, payload) {
      state.configs.forEach(function (part, index) {
        if (state.configs[index].id == payload.configId)
          state.configs[index].munition_id = payload.id;
      });
    },
    updateConfigCannon(state, payload) {
      state.configs.forEach(function (part, index) {
        if (state.configs[index].id == payload.configId)
          state.configs[index].cannon_id = payload.id;
      });
    }
  },
  actions: {
  },
  modules: {
  }
})
