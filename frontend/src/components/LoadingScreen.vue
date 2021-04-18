<template>
  <v-card style="margin: 20px; padding: 10px">
    <v-card-subtitle style="text-align: center">
      <h2>{{ title }}</h2>
      <div style="margin: 15px 0">Loading data</div>
    </v-card-subtitle>
    <v-card-text style="text-align: center">
      <v-progress-circular
        :size="70"
        :width="7"
        color="primary"
        indeterminate
      ></v-progress-circular>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: "LoadingScreen",
  props: ["title"],
};
</script>