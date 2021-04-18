<template>
  <v-card class="mx-auto" max-width="400" outlined>
    <v-card-title>
      {{ config.name }}
    </v-card-title>
    <v-container>
      <v-row align="center">
        <v-col cols="12" md="8">
          <v-img
            :src="require('../assets/' + gun_img + '.png')"
            width="200"
            contain
          />
        </v-col>
        <v-col cols="12" md="4">
          <v-checkbox v-model="checkbox" :label="'Display'"> </v-checkbox>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: "SimulatorConfigElement",
  data() {
    return {
      checkbox: "",
    };
  },
  computed: {
    platform() {
      return this.$store.state.platforms.find(
        (platform) => platform.id == this.config.platform
      );
    },
    gun_img() {
      if (this.platform == null) return "gun";
      else {
        const letter = this.platform.name[1];
        return letter == "R" ? "gun_ar" : "gun";
      }
    },
  },
  watch: {
    checkbox: function (newValue) {
      const configId = this.config.id;
      const show = newValue;
      this.$store.commit("switchConfigDisplay", { configId, show });
    },
  },
  created: function () {
    const displayedConfigs = this.$store.state.displayedConfigs;
    this.checkbox = displayedConfigs.indexOf(this.config.id) >= 0 ? true : false;    
  },
  props: ["config"],
};
</script>
