<template>
  <div class="configuration">
    <v-container class="grey lighten-5" fluid>
      <v-row v-if="!loadingData">
        <v-col cols="12" sm="4">
          <v-card class="pa-2" outlined tile>
            <v-container>
              <v-row>
                <v-col>
                  <h4>Configuration selection</h4>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" sm="9">
                  <v-select
                    v-model="selectedConfigId"
                    :items="configs"
                    item-text="name"
                    item-value="id"
                    label="Configuration"
                  ></v-select>
                </v-col>
                <v-col cols="12" sm="3">
                  <v-btn block color="error" v-on:click="deleteConfig">
                    <v-icon>mdi-trash-can</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <h4>Configuration creation</h4>
                </v-col>
              </v-row>
              <v-row>
                <v-col cols="12" sm="9">
                  <v-text-field
                    v-model="newConfigName"
                    placeholder="New configuration name"
                    solo
                    dense
                  ></v-text-field>
                </v-col>
                <v-col cols="12" sm="3">
                  <v-btn block color="success" v-on:click="createConfig">
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
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
              <v-row v-else>
                <v-col>
                  <v-alert
                    type="info"
                    border="right"
                    colored-border
                    elevation="2"
                  >
                    <b>Components:</b> please select a configuration.
                  </v-alert>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-img
                    :src="require('../assets/' + gun_img + '.png')"
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
            <div v-else>
              <v-alert type="info" border="right" colored-border elevation="2">
                <b>Details:</b> please select a configuration.
              </v-alert>
            </div>
          </v-card>
        </v-col>
      </v-row>
      <v-row v-else>
        <v-spacer></v-spacer>
        <v-col>
          <loading-screen />
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
    </v-container>

    <snackbar-info
      :snackbar="snackbar"
      :timeout="snackbarTimeout"
      :text="snackbarText"
    />
  </div>
</template>

<script>
// @ is an alias to /src
import GunComponentList from "@/components/GunComponentList.vue";
import GunComponentCardDroppable from "@/components/GunComponentCardDroppable.vue";
import GunProgressBar from "@/components/GunProgressBar.vue";
import LoadingScreen from "@/components/LoadingScreen.vue";
import SnackbarInfo from "@/components/SnackbarInfo.vue";

export default {
  name: "Configuration",
  components: {
    GunComponentList,
    GunComponentCardDroppable,
    GunProgressBar,
    LoadingScreen,
    SnackbarInfo,
  },
  data() {
    return {
      selectedConfigId: null,
      selectedPlatform: null,
      selectedAmmo: null,
      selectedCannon: null,
      newConfigName: null,
      weight: 0,
      price: 0,
      length: 0,
      snackbar: false,
      snackbarText: "Something happened.",
      snackbarTimeout: 2000,
    };
  },
  computed: {
    loadingData() {
      return (
        this.platforms.length <= 0 ||
        this.ammos.length <= 0 ||
        this.cannons.length <= 0
      );
    },
    gun_img() {
      if (this.selectedPlatform == null) return "gun";
      else {
        const letter = this.selectedPlatform.name[1];
        return letter == "R" ? "gun_ar" : "gun";
      }
    },
    configs() {
      return Object.values(this.$store.state.configs);
    },
    selectedConfigPlatformId() {
      if (this.selectedConfigId != null)
        return this.$store.state.configs.find(
          (config) => config.id == this.selectedConfigId
        ).platform;
      else return null;
    },
    selectedConfigAmmoId: function () {
      if (this.selectedConfigId != null)
        return this.$store.state.configs.find(
          (config) => config.id == this.selectedConfigId
        ).ammo;
      else return null;
    },
    selectedConfigCannonId: function () {
      if (this.selectedConfigId != null)
        return this.$store.state.configs.find(
          (config) => config.id == this.selectedConfigId
        ).cannon;
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
      return (this.weight / 5.5) * 100.0;
    },
    priceProgress() {
      return (this.price / 2250.0) * 100.0;
    },
    lenghtProgress() {
      return (this.length / 100.0) * 100.0;
    },
  },
  methods: {
    createConfig() {
      if (this.loadingData) console.log("Operation aborted: not enough data.");
      else {
        const name =
          this.newConfigName != null ? this.newConfigName : "newConfig";
        const cannon = this.cannons[0].id;
        const ammo = this.ammos[0].id;
        const platform = this.platforms[0].id;

        this.$store.dispatch("postConfig", {
          name: name,
          cannon: cannon,
          ammo: ammo,
          platform: platform,
        });
      }
    },
    deleteConfig() {
      if (this.selectedConfigId == null)
        console.log("Operation aborted: no configuration selected.");
      else {
        this.$store.dispatch("deleteConfig", this.selectedConfigId);
        this.selectedConfigId = null;
      }
    },
    updateConfig(configId) {
      const config = this.$store.state.configs.find(
        (config) => config.id == configId
      );

      if (config != null) {
        this.selectedPlatform = this.$store.state.platforms.find(
          (platform) => platform.id == config.platform
        );
        this.selectedAmmo = this.$store.state.ammos.find(
          (ammo) => ammo.id == config.ammo
        );
        this.selectedCannon = this.$store.state.cannons.find(
          (cannon) => cannon.id == config.cannon
        );

        this.weight =
          parseFloat(this.selectedPlatform.weight) +
          parseFloat(this.selectedAmmo.weight) +
          parseFloat(this.selectedCannon.weight);
        this.weight = this.weight.toFixed(1);
        this.price =
          parseFloat(this.selectedPlatform.price) +
          parseFloat(this.selectedAmmo.price * 30) +
          parseFloat(this.selectedCannon.price);
        this.price = this.price.toFixed(1);
        this.length =
          100 *
          (parseFloat(this.selectedPlatform.length) -
            parseFloat(this.selectedPlatform.standard_cannon_length) +
            parseFloat(this.selectedCannon.length));
        this.length = this.length.toFixed(1);
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
    configs: function () {
      this.snackbarText = "Configurations updated.";
      this.snackbar = true;
    },
    platforms: function () {},
    ammos: function () {},
    cannons: function () {},
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
