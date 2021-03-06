define ['angular', 'jquery', 'prettify'], (angular, $, prettify) ->
    module = angular.module 'coviolations.directives', []

    module.directive 'fullfill', ->
        (scope, element) ->
            $el = $(element)
            $el.attr 'width', $el.parent().width() + 21

    module.directive 'forAuthenticated', ->
        (scope, element) ->
            $(element).css 'display', 'none' if not window.isAuthenticated

    module.directive 'forAnonymouse', ->
        (scope, element) ->
            $(element).css 'display', 'none' if window.isAuthenticated

    module.directive 'prettifyChilds', ->
        (scope, element) ->
            setTimeout =>
                $(element).find('pre').each (n, el) =>
                    $(el).html prettify.prettyPrintOne $(el).html()
                    $(el).addClass 'prettyprinted'
            , 100
