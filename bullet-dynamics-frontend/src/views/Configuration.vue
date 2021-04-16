<template>
  <div class="configuration">
    <v-container class="grey lighten-5">
      <v-row>
        <v-col cols="12" sm="6">
          <v-card class="pa-2" outlined tile>
            <v-container>
              <v-row>
                <v-col cols="12" sm="6">
                  <v-select
                    v-model="selectedConfig"
                    :items="configs"
                    item-text="name"
                    item-value="id"
                    label="Configuration"
                  ></v-select>
                </v-col>
                <v-col cols="12" sm="3">
                  <v-btn block color="success"><v-icon>mdi-plus</v-icon></v-btn>
                </v-col>
                <v-col cols="12" sm="3">
                  <v-btn block color="error"
                    ><v-icon>mdi-trash-can</v-icon></v-btn
                  >
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <h2>Platforms</h2>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="3" :key="platform" v-for="platform in platforms">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <v-card v-bind="attrs" v-on="on">
                        <v-card-text style="padding: 0">
                          <v-img
                            :src="require('../assets/gun_icon.png')"
                            contain
                            height="50"
                          />
                        </v-card-text>
                      </v-card>
                    </template>
                    <span>
                      {{ platform.desc }}: {{ platform.weight }}g,
                      {{ platform.price }}$, {{ platform.length }}cm
                    </span>
                  </v-tooltip>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <h2>Ammunition</h2>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  cols="3"
                  :key="ammunition"
                  v-for="ammunition in ammunitions"
                >
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <v-card v-bind="attrs" v-on="on">
                        <v-card-text style="padding: 0">
                          <v-img
                            :src="require('../assets/ammunition_icon.png')"
                            contain
                            height="50"
                          />
                        </v-card-text>
                      </v-card>
                    </template>
                    <span>
                      {{ ammunition.desc }}: {{ ammunition.weight }}g,
                      {{ ammunition.price }}$
                    </span>
                  </v-tooltip>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <h2>Cannons</h2>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="3" :key="cannon" v-for="cannon in cannons">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <v-card v-bind="attrs" v-on="on">
                        <v-card-text style="padding: 0">
                          <v-img
                            :src="require('../assets/cannon_icon.png')"
                            contain
                            height="50"
                          />
                        </v-card-text>
                      </v-card>
                    </template>
                    <span>
                      {{ cannon.desc }}: {{ cannon.weight }}g,
                      {{ cannon.price }}$, {{ cannon.length }}cm
                    </span>
                  </v-tooltip>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>
        <v-col cols="12" sm="6">
          <v-card class="pa-2" outlined tile>
            <v-container>
              <v-row>
                <v-col cols="12" sm="4">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <v-card v-bind="attrs" v-on="on">
                        <v-card-text style="padding: 0">
                          <v-img
                            :src="require('../assets/gun_icon.png')"
                            contain
                            height="50"
                          />
                        </v-card-text>
                      </v-card>
                    </template>
                    <span>
                      {{ selectedPlatform.desc }}:
                      {{ selectedPlatform.weight }}g,
                      {{ selectedPlatform.price }}$,
                      {{ selectedPlatform.length }}cm
                    </span>
                  </v-tooltip>
                </v-col>
                <v-col cols="12" sm="4">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <v-card v-bind="attrs" v-on="on">
                        <v-card-text style="padding: 0">
                          <v-img
                            :src="require('../assets/ammunition_icon.png')"
                            contain
                            height="50"
                          />
                        </v-card-text>
                      </v-card>
                    </template>
                    <span>
                      {{ selectedAmmunition.desc }}:
                      {{ selectedAmmunition.weight }}g,
                      {{ selectedAmmunition.price }}$
                    </span>
                  </v-tooltip>
                </v-col>
                <v-col cols="12" sm="4">
                  <v-tooltip bottom>
                    <template v-slot:activator="{ on, attrs }">
                      <v-card v-bind="attrs" v-on="on">
                        <v-card-text style="padding: 0">
                          <v-img
                            :src="require('../assets/cannon_icon.png')"
                            contain
                            height="50"
                          />
                        </v-card-text>
                      </v-card>
                    </template>
                    <span>
                      {{ selectedCannon.desc }}: {{ selectedCannon.weight }}g,
                      {{ selectedCannon.price }}$, {{ selectedCannon.length }}cm
                    </span>
                  </v-tooltip>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-img
                    :src="require('../assets/gun.png')"
                    contain
                    height="200"
                  />
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" sm="2">
                  Weight:
                </v-col>
                <v-col cols="12" sm="8">
                  <v-progress-linear
                    v-model="totalWeightProgress"
                    color="red"
                    height="25"
                  ></v-progress-linear>
                </v-col>
                <v-col cols="12" sm="2">
                  {{totalWeight}} kg
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" sm="2">
                  Price:
                </v-col>
                <v-col cols="12" sm="8">
                  <v-progress-linear
                    v-model="totalPriceProgress"
                    color="amber"
                    height="25"
                  ></v-progress-linear>
                </v-col>
                <v-col cols="12" sm="2">
                  {{totalPrice}} $
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" sm="2">
                  Length:
                </v-col>
                <v-col cols="12" sm="8">
                  <v-progress-linear
                    v-model="totalLenghtProgress"
                    color="green"
                    height="25"
                  ></v-progress-linear>
                </v-col>
                <v-col cols="12" sm="2">
                  {{totalLength}} cm
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Configuration",
  components: {
    //HelloWorld,
  },
  data() {
    return {
      selectedConfig: null,
      selectedPlatform: {
        id: 0,
        desc: "Platform alpha",
        weight: 2,
        price: 500,
        length: 80,
        standard_cannon_length: 20,
      },
      selectedAmmunition: {
        id: 0,
        desc: "Ammunition alpha",
        weight: 0.2,
        price: 40,
        bullet_weight: 0,
        cx: 0,
      },
      selectedCannon: {
        id: 0,
        desc: "Cannon alpha",
        weight: 1,
        price: 100,
        length: 15,
      },
    };
  },
  computed: {
    configs() {
      return this.$store.state.configs;
    },
    platforms() {
      return this.$store.state.platforms;
    },
    ammunitions() {
      return this.$store.state.ammunitions;
    },
    cannons() {
      return this.$store.state.cannons;
    },
    totalWeight() {
      return this.selectedPlatform.weight + this.selectedAmmunition.weight + this.selectedCannon.weight;
    },
    totalWeightProgress() {
      return this.totalWeight / 5.0 * 100.0;
    },
    totalPrice() {
      return this.selectedPlatform.price + this.selectedAmmunition.price + this.selectedCannon.price;
    },
    totalPriceProgress() {
      return this.totalPrice / 3000.0 * 100.0;
    },
    totalLength() {
      return this.selectedPlatform.length + this.selectedPlatform.standard_cannon_length + this.selectedCannon.length;
    },
    totalLenghtProgress() {
      return this.totalLength / 120.0 * 100.0;
    }
  },
};
</script>
