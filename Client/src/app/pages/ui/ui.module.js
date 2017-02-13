/**
 * @author k.danovsky
 * created on 12.01.2016
 */
(function () {
  'use strict';

  angular.module('zAdmin.pages.ui', [
    'zAdmin.pages.ui.typography',
    'zAdmin.pages.ui.buttons',
    'zAdmin.pages.ui.icons',
    'zAdmin.pages.ui.modals',
    'zAdmin.pages.ui.grid',
    'zAdmin.pages.ui.alerts',
    'zAdmin.pages.ui.progressBars',
    'zAdmin.pages.ui.notifications',
    'zAdmin.pages.ui.tabs',
    'zAdmin.pages.ui.slider',
    'zAdmin.pages.ui.panels'
  ])
      .config(routeConfig);

  /** @ngInject */
  function routeConfig($stateProvider) {
    $stateProvider
        .state('ui', {
          url: '/ui',
          template : '<ui-view></ui-view>',
          abstract: true,
          title: 'UI Features',
          sidebarMeta: {
            icon: 'ion-android-laptop',
            order: 200
          },
        });
  }

})();
