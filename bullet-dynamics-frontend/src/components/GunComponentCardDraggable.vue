<template>
  <v-tooltip bottom>
    <template v-slot:activator="{ on, attrs }">
      <v-card v-bind="attrs" v-on="on">
        <v-card-text style="padding: 0">
          <v-img
            :src="require('../assets/' + imgSrc + '_icon.png')"
            contain
            height="50"
            draggable
            @dragstart="drag($event)"
          />
        </v-card-text>
      </v-card>
    </template>
    <span>
      {{ tooltip(component) }}
    </span>
  </v-tooltip>
</template>


<script>
export default {
  name: "GunComponentCardDraggable",
  data() {
    return {};
  },
  computed: {
    imgSrc() {
      if (this.type == "platform") return "gun";
      else if (this.type == "ammunition") return "ammunition";
      else return "cannon";
    },
  },
  methods: {
    drag(event) {
      event.dataTransfer.setData("type", this.type);
      event.dataTransfer.setData("id", this.component.id);
    },
    tooltip(component) {
      if (this.type == "platform") {
        return (
          component.desc +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$, " +
          component.length +
          "cm"
        );
      } else if (this.type == "ammunition") {
        return (
          component.desc +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$"
        );
      } else {
        return (
          component.desc +
          ": " +
          component.weight +
          "g, " +
          component.price +
          "$, " +
          component.length +
          "cm"
        );
      }
    },
  },
  props: ["type", "component"],
};
</script>