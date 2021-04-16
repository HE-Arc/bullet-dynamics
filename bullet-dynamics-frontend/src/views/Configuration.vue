<template>
  <div class="configuration">
    <v-container class="grey lighten-5">
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
            <gun-component-list name="Ammunition" :components="ammunitions" />
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
                    type="ammunition"
                    :configId="selectedConfigId"
                    :component="selectedAmmunition"
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
        <v-col>
          Loading...
        </v-col>
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
      selectedAmmunition: null,
      selectedCannon: null,
      weight: 0,
      price: 0,
      length: 0,
    };
  },
  computed: {
    loadingData() {
      return (
        this.configs == null ||
        this.platforms == null ||
        this.ammunitions == null ||
        this.cannons == null
      );
    },
    configs() {
      return this.$store.state.configs;
    },
    selectedConfigPlatformId() {
      if (this.selectedConfigId != null)
        return this.$store.state.configs.find(
          (config) => config.id == this.selectedConfigId
        ).plateform_id;
      else return null;
    },
    selectedConfigAmmunitionId: function () {
      if (this.selectedConfigId != null)
        return this.$store.state.configs.find(
          (config) => config.id == this.selectedConfigId
        ).munition_id;
      else return null;
    },
    selectedConfigCannonId: function () {
      if (this.selectedConfigId != null)
        return this.$store.state.configs.find(
          (config) => config.id == this.selectedConfigId
        ).cannon_id;
      else return null;
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
      const config = this.$store.state.configs.find(
        (config) => config.id == configId
      );

      if (config != null) {
        this.selectedPlatform = this.$store.state.platforms.find(
          (component) => component.id == config.plateform_id
        );
        this.selectedAmmunition = this.$store.state.ammunitions.find(
          (component) => component.id == config.munition_id
        );
        this.selectedCannon = this.$store.state.cannons.find(
          (component) => component.id == config.cannon_id
        );

        this.weight =
          this.selectedPlatform.weight +
          this.selectedAmmunition.weight +
          this.selectedCannon.weight;
        this.price =
          this.selectedPlatform.price +
          this.selectedAmmunition.price +
          this.selectedCannon.price;
        this.length =
          this.selectedPlatform.length +
          this.selectedPlatform.standard_cannon_length +
          this.selectedCannon.length;
      } else {
        this.selectedPlatform = null;
        this.selectedAmmunition = null;
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
    selectedConfigAmmunitionId: function () {
      this.updateConfig(this.selectedConfigId);
    },
    selectedConfigCannonId: function () {
      this.updateConfig(this.selectedConfigId);
    },
  },
  created: function () {
    const configs = this.$store.state.configs;
    const platforms = this.$store.state.platforms;
    const ammunitions = this.$store.state.ammunitions;
    const cannons = this.$store.state.cannons;

    if (configs == null) this.$store.dispatch("fetchConfigs");
    if (platforms == null) this.$store.dispatch("fetchPlatforms");
    if (ammunitions == null) this.$store.dispatch("fetchAmmunitions");
    if (cannons == null) this.$store.dispatch("fetchCannons");
  },
};
</script>
