var app = angular.module('mathApp', []);

app.controller('mathController', function($scope, $http) {
    $scope.submitForm = function() {
        var data = {
            num1: $scope.num1,
            num2: $scope.num2
        };
        var url = '/' + $scope.operation;
        $http.post(url, data).then(function(response) {
            if ('result' in response.data) {
                $scope.result = response.data.result;
                $scope.error = '';
            } else {
                $scope.error = response.data.error;
                $scope.result = '';
            }
        });
    };
});