<template>
  <v-card class="mx-auto" max-width="500" outlined>
    <v-form ref="form">
      <v-container>
        <v-row justify="space-between">
          <v-col cols="6">
            <v-text-field
              v-model="height"
              type="number"
              :rules="rules"
              label="Height"
              :disabled="true"
            ></v-text-field>
          </v-col>
          <v-col cols="6">
            <v-text-field
              v-model="angle"
              type="number"
              :rules="rules"
              label="Angle"
              :disabled="true"
            ></v-text-field>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </v-card>
</template>

<script>
export default {
  name: "SimulatorParamList",

  data: () => ({
    height: 0,
    angle: 0,
  }),
};
</script>
