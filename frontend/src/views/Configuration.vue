<template>
  <div class="configuration">
    <v-container class="grey lighten-5" fluid>
      <v-row v-if="!loadingData">
        <v-col cols="12" sm="4">
          <v-card class="pa-2" outlined tile>
            <v-container>
              <v-row>
                <v-col cols="12" sm="6">
                  <v-select
                    v-model="selectedConfigId"
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
            </v-container>
            <gun-component-list name="Platforms" :components="platforms" />
            <gun-component-list name="Ammo" :components="ammos" />
            <gun-component-list name="Cannons" :components="cannons" />
          </v-card>
        </v-col>
        <v-col cols="12" sm="8">
          <v-card class="pa-2" outlined tile>
            <v-container>
              <v-row v-if="selectedConfigId != null">
                <v-col cols="12" sm="4">
                  <gun-component-card-droppable
                    type="platform"
                    :configId="selectedConfigId"
                    :component="selectedPlatform"
                  />
                </v-col>
                <v-col cols="12" sm="4">
                  <gun-component-card-droppable
                    type="ammo"
                    :configId="selectedConfigId"
                    :component="selectedAmmo"
                  />
                </v-col>
                <v-col cols="12" sm="4">
                  <gun-component-card-droppable
                    type="cannon"
                    :configId="selectedConfigId"
                    :component="selectedCannon"
                  />
                </v-col>
              </v-row>
              <v-row v-else> Sélectionne une config PD! </v-row>
              <v-row>
                <v-col>
                  <v-img
                    :src="require('../assets/gun.png')"
                    contain
                    height="200"
                  />
                </v-col>
              </v-row>
            </v-container>
            <div v-if="selectedConfigId != null">
              <gun-progress-bar
                name="Weight"
                unit="kg"
                color="red"
                :total="weight"
                :progress="weightProgress"
              />
              <gun-progress-bar
                name="Price"
                unit="$"
                color="amber"
                :total="price"
                :progress="priceProgress"
              />
              <gun-progress-bar
                name="Length"
                unit="cm"
                color="green"
                :total="length"
                :progress="lenghtProgress"
              />
            </div>
            <div v-else>Sélectionne une config PD!</div>
          </v-card>
        </v-col>
      </v-row>
      <v-row v-else>
        <v-spacer></v-spacer>
        <v-col>
          <v-card style="margin: 20px; padding: 10px">
            <v-card-subtitle style="text-align: center">
              <h2>CONFIGURATION</h2>
              <div style="margin: 15px 0">Loading data</div>
            </v-card-subtitle>
            <v-card-text style="text-align: center">
              <v-progress-circular
                :size="70"
                :width="7"
                color="primary"
                indeterminate
              ></v-progress-circular>
              {{configs}}
              {{platforms}}
              {{ammos}}
              {{cannons}}
            </v-card-text>
          </v-card>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import GunComponentList from "@/components/GunComponentList.vue";
import GunComponentCardDroppable from "@/components/GunComponentCardDroppable.vue";
import GunProgressBar from "@/components/GunProgressBar.vue";

export default {
  name: "Configuration",
  components: {
    GunComponentList,
    GunComponentCardDroppable,
    GunProgressBar,
  },
  data() {
    return {
      selectedConfigId: null,
      selectedPlatform: null,
      selectedAmmo: null,
      selectedCannon: null,
      weight: 0,
      price: 0,
      length: 0,
    };
  },
  computed: {
    loadingData() {
      return (
        this.configs.length <= 0 ||
        this.platforms.length <= 0 ||
        this.ammos.length <= 0 ||
        this.cannons.length <= 0
      );
    },
    configs() {
      return Object.values(this.$store.state.configs);
    },
    selectedConfigPlatformId() {
      if (this.selectedConfigId != null)
        return this.$store.state.configs[this.selectedConfigId].platform_id;
      else return null;
    },
    selectedConfigAmmoId: function () {
      if (this.selectedConfigId != null)
        return this.$store.state.configs[this.selectedConfigId].ammo_id;
      else return null;
    },
    selectedConfigCannonId: function () {
      if (this.selectedConfigId != null)
        return this.$store.state.configs[this.selectedConfigId].cannon_id;
      else return null;
    },
    platforms() {
      return this.$store.state.platforms;
    },
    ammos() {
      return this.$store.state.ammos;
    },
    cannons() {
      return this.$store.state.cannons;
    },
    weightProgress() {
      return (this.weight / 5.0) * 100.0;
    },
    priceProgress() {
      return (this.price / 3000.0) * 100.0;
    },
    lenghtProgress() {
      return (this.length / 120.0) * 100.0;
    },
  },
  methods: {
    updateConfig(configId) {
      const config = this.$store.state.configs[configId];

      if (config != null) {
        this.selectedPlatform = this.$store.state.platforms[config.platform_id];
        this.selectedAmmo = this.$store.state.ammos[config.ammo_id];
        this.selectedCannon = this.$store.state.cannons[config.cannon_id];

        //TODO cast to int 
        this.weight =
          parseFloat(this.selectedPlatform.weight) +
          parseFloat(this.selectedAmmo.weight) +
          parseFloat(this.selectedCannon.weight);
        this.price =
          parseFloat(this.selectedPlatform.price) +
          parseFloat(this.selectedAmmo.price) +
          parseFloat(this.selectedCannon.price);
        this.length = 100 * (
          parseFloat(this.selectedPlatform.length) -
          parseFloat(this.selectedPlatform.standard_cannon_length) +
          parseFloat(this.selectedCannon.length));
      } else {
        this.selectedPlatform = null;
        this.selectedAmmo = null;
        this.selectedCannon = null;

        this.weight = 0;
        this.price = 0;
        this.length = 0;
      }
    },
  },
  watch: {
    selectedConfigId: function (newConfigId) {
      this.updateConfig(newConfigId);
    },
    selectedConfigPlatformId: function () {
      this.updateConfig(this.selectedConfigId);
    },
    selectedConfigAmmoId: function () {
      this.updateConfig(this.selectedConfigId);
    },
    selectedConfigCannonId: function () {
      this.updateConfig(this.selectedConfigId);
    },
    configs: function (nv) {
      console.log(nv);
    },
    platforms: function (nv) {
      console.log(nv);
    },
    ammos: function (nv) {
      console.log(nv);
    },
    cannons: function (nv) {
      console.log(nv);
    },
  },
  created: function () {
    const configs = this.$store.state.configs;
    const platforms = this.$store.state.platforms;
    const ammos = this.$store.state.ammos;
    const cannons = this.$store.state.cannons;

    if (configs.length <= 0) this.$store.dispatch("fetchConfigs");
    if (platforms.length <= 0) this.$store.dispatch("fetchPlatforms");
    if (ammos.length <= 0) this.$store.dispatch("fetchAmmos");
    if (cannons.length <= 0) this.$store.dispatch("fetchCannons");
  },
};
</script>