'use strict';

angular.module('adomattic.dashboard')
  .controller('CampaignListCtrl', function($mdDialog, $location, urls, Campaign) {
    var self = this;

    self.campaigns = Campaign.query();

    self.showPreview = function(ev, data) {
      $mdDialog.show({
        controller: 'CampaignPreviewDialogCtrl',
        controllerAs: 'previewController',
        templateUrl: urls.partials.dialogs + 'campaigns/preview.html',
        locals: {
          data: data
        },
        targetEvent: ev,
        parent: angular.element(document.body)
      });
    };

    self.openStripePaymentDialog = function(invoiceID) {
      $mdDialog.show({
        controller: 'StripeCreditCardDialogCtrl',
        controllerAs: 'creditCard',
        templateUrl: urls.partials.dialogs + 'payments/stripe-credit-card.html',
        locals: {
          invoiceID: invoiceID
        },
        //targetEvent: ev,
        parent: angular.element(document.body)
      }).then(function() {
        self.campaigns = Campaign.query();
      });
    };

    self.editCampaign = function (campaignID) {
      var p = '/campaigns/' + campaignID + '/edit/';
      console.log(p);
      $location.path(p);
    };
  });
