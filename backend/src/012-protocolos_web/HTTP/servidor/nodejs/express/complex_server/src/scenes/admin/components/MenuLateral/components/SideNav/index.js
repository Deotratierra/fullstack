angular
  .module('SideNav',['ngMaterial'])
  .controller('SideNavCtrl', ["$scope","$mdSidenav", ($scope, $mdSidenav) => {
    $scope.toggleLeft = buildToggler('left');
    $scope.toggleRight = buildToggler('right');

    function buildToggler(componentId) {
      return function() {
        $mdSidenav(componentId).toggle();
      };
    };
  }]);


