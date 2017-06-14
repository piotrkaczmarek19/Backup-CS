app.controller('DayController', ['$scope', 'events', function($scope,events) {
    events.success(function(data){
        console.log('controller works')
        $scope.day = data;
    })
}]);