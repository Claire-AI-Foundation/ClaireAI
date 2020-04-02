<template>
  <v-app-bar
    :clipped-left="$bp.lgAndUp"
    app
    color="blue darken-3"
    dark
    dense
    flat
  >
    <v-app-bar-nav-icon @click.stop="$emit('toggle-drawer', true)"></v-app-bar-nav-icon>
    <v-toolbar-title
      class="ml-0 pl-md-3"
    >

      <span class="hidden-sm-and-down">{{$appName}}</span>
    </v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn icon class="mr-3">
      <v-icon>mdi-bell</v-icon>
    </v-btn>

    <v-menu transition="slide-y-transition" offset-y v-if="user">
      <template v-slot:activator="{on}">
        <v-btn text v-on="on" class="mt-1" :icon="$bp.xsOnly">
          <template>
            <v-avatar
              size="36"
              :color="$helpers.colorMinder(user.name)"
            >
              <img v-if="user && user.photo" :src="user.photo" alt="avatar">
              <span v-else class="white--text headline text-capitalize">
                {{user.name.charAt(0)}}
              </span>
            </v-avatar>
            <v-icon dark class="mr-3">mdi-menu-down</v-icon>
          </template>
        </v-btn>
      </template>

      <v-list dense>

        <v-list-item :to="'/profile'">
          <v-icon color="success">mdi-account</v-icon>
          <v-list-item-title style="margin-left:5px;">My Profile</v-list-item-title>
        </v-list-item>
        <v-list-item to="/settings">
          <v-icon color="cyan">mdi-settings</v-icon>
          <v-list-item-title style="margin-left:5px;">Settings</v-list-item-title>
        </v-list-item>

        <v-divider></v-divider>

        <v-list-item @click="$store.dispatch('logout')">
          <v-list-item-title style="margin-left:5px;">Logout</v-list-item-title>
        </v-list-item>
      </v-list>
      </v-menu>
  </v-app-bar>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'TopBar',

  data: () => ({
  }),
  computed: {
    ...mapGetters([
      'getUser'
    ]),
    $bp () {
      return this.$vuetify.breakpoint
    },
    user () {
      return this.getUser
    }
  }
}
</script>
