(function () {
  'use strict';

  angular.module('zAdmin.pages.auth', [])
  .config(routeConfig);

  /** @ngInject */
    function routeConfig($stateProvider) {
      $stateProvider
          .state('auth', {
            url: '/auth',
            templateUrl: 'app/pages/auth/auth.html',
            title: 'Login',
            controller: 'authCtrl',
            controllerAs: 'vm',
            sidebarMeta: {
              icon: 'ion-android-person',
              order: 1
            }
          });
    }

})();