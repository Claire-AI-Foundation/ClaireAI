<template>
  <v-app>
    <top-bar @toggle-drawer="toggleDrawer"/>

    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="mini"
      :clipped="$bp.lgAndUp"
      app
    >
      <v-list dense flat>
        <template v-for="item in items">
          <v-list-item
            :key="item.text"
            :to="item.link"
            active-class="primary--text"
          >
            <v-list-item-action>
              <v-icon :color="item.color || ''">
                {{ item.icon }}
              </v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>
                {{ item.text }}
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-list>
      <sidebar-footer :mini="mini"></sidebar-footer>
    </v-navigation-drawer>

    <v-content>
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import TopBar from '@/components/TopBar'
import SidebarFooter from '@/components/SidebarFooter'

export default {
  name: 'Home',
  data: () => ({
    dialog: false,
    drawer: null,
    mini: false,
    items: [
      { icon: 'mdi-home', text: 'Home', link: '/' },
      { icon: 'mdi-heart', text: 'Medical Report', color: 'red' },
      { icon: 'mdi-history', text: 'Medical History' },
      // { icon: 'mdi-account-outline', text: 'Your Profile' },
      { icon: 'mdi-cog-outline', text: 'Settings' },
      { icon: 'mdi-chat-outline', text: 'Send feedback' },
      { icon: 'mdi-lifebuoy', text: 'Helpline/Emergency', link: '/help' },
      { icon: 'mdi-information-variant', text: 'About', link: '/about' }
    ]
  }),
  computed: {
    $bp () {
      return this.$vuetify.breakpoint
    }
  },
  components: {
    TopBar,
    SidebarFooter
  },
  methods: {
    toggleDrawer () {
      if (this.$bp.smAndDown) {
        this.drawer = !this.drawer
        this.mini = false
      } else {
        this.drawer = true
        this.mini = !this.mini
      }
    }
  }
}
</script>
