<template>
  <v-card class="mx-auto" max-width="400" outlined>
    <v-card-title>
      {{ name }}
    </v-card-title>
    <v-container>
      <v-row align="center">
        <v-col cols="8">
          <v-img :src="require('../assets/m16a4-small.png')"> </v-img>
        </v-col>
        <v-col cols="4">
          <v-checkbox v-model="checkbox" :label="'display'"> </v-checkbox>
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
  props: ["name"],
};
</script>
