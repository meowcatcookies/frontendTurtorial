import sublime_plugin
import sublime

bootstrap_441_classes = ["accordion","active","alert","alert-danger","alert-dark","alert-dismissible","alert-heading","alert-info","alert-light","alert-link","alert-primary","alert-secondary","alert-success","alert-warning","align-baseline","align-bottom","align-content-around","align-content-between","align-content-center","align-content-end","align-content-lg-around","align-content-lg-between","align-content-lg-center","align-content-lg-end","align-content-lg-start","align-content-lg-stretch","align-content-md-around","align-content-md-between","align-content-md-center","align-content-md-end","align-content-md-start","align-content-md-stretch","align-content-sm-around","align-content-sm-between","align-content-sm-center","align-content-sm-end","align-content-sm-start","align-content-sm-stretch","align-content-start","align-content-stretch","align-content-xl-around","align-content-xl-between","align-content-xl-center","align-content-xl-end","align-content-xl-start","align-content-xl-stretch","align-items-baseline","align-items-center","align-items-end","align-items-lg-baseline","align-items-lg-center","align-items-lg-end","align-items-lg-start","align-items-lg-stretch","align-items-md-baseline","align-items-md-center","align-items-md-end","align-items-md-start","align-items-md-stretch","align-items-sm-baseline","align-items-sm-center","align-items-sm-end","align-items-sm-start","align-items-sm-stretch","align-items-start","align-items-stretch","align-items-xl-baseline","align-items-xl-center","align-items-xl-end","align-items-xl-start","align-items-xl-stretch","align-middle","align-self-auto","align-self-baseline","align-self-center","align-self-end","align-self-lg-auto","align-self-lg-baseline","align-self-lg-center","align-self-lg-end","align-self-lg-start","align-self-lg-stretch","align-self-md-auto","align-self-md-baseline","align-self-md-center","align-self-md-end","align-self-md-start","align-self-md-stretch","align-self-sm-auto","align-self-sm-baseline","align-self-sm-center","align-self-sm-end","align-self-sm-start","align-self-sm-stretch","align-self-start","align-self-stretch","align-self-xl-auto","align-self-xl-baseline","align-self-xl-center","align-self-xl-end","align-self-xl-start","align-self-xl-stretch","align-text-bottom","align-text-top","align-top","arrow","badge","badge-danger","badge-dark","badge-info","badge-light","badge-pill","badge-primary","badge-secondary","badge-success","badge-warning","bg-danger","bg-dark","bg-info","bg-light","bg-primary","bg-secondary","bg-success","bg-transparent","bg-warning","bg-white","blockquote","blockquote-footer","border","border-0","border-bottom","border-bottom-0","border-danger","border-dark","border-info","border-left","border-left-0","border-light","border-primary","border-right","border-right-0","border-secondary","border-success","border-top","border-top-0","border-warning","border-white","breadcrumb","breadcrumb-item","bs-popover-auto","bs-popover-bottom","bs-popover-left","bs-popover-right","bs-popover-top","bs-tooltip-auto","bs-tooltip-bottom","bs-tooltip-left","bs-tooltip-right","bs-tooltip-top","btn","btn-block","btn-danger","btn-dark","btn-group","btn-group-lg","btn-group-sm","btn-group-toggle","btn-group-vertical","btn-info","btn-lg","btn-light","btn-link","btn-outline-danger","btn-outline-dark","btn-outline-info","btn-outline-light","btn-outline-primary","btn-outline-secondary","btn-outline-success","btn-outline-warning","btn-primary","btn-secondary","btn-sm","btn-success","btn-toolbar","btn-warning","card","card-body","card-columns","card-deck","card-footer","card-group","card-header","card-header-pills","card-header-tabs","card-img","card-img-bottom","card-img-overlay","card-img-top","card-link","card-subtitle","card-text","card-title","carousel","carousel-caption","carousel-control-next","carousel-control-next-icon","carousel-control-prev","carousel-control-prev-icon","carousel-fade","carousel-indicators","carousel-inner","carousel-item","carousel-item-left","carousel-item-next","carousel-item-prev","carousel-item-right","clearfix","close","col","col-1","col-10","col-11","col-12","col-2","col-3","col-4","col-5","col-6","col-7","col-8","col-9","col-auto","col-form-label","col-form-label-lg","col-form-label-sm","col-lg","col-lg-1","col-lg-10","col-lg-11","col-lg-12","col-lg-2","col-lg-3","col-lg-4","col-lg-5","col-lg-6","col-lg-7","col-lg-8","col-lg-9","col-lg-auto","col-md","col-md-1","col-md-10","col-md-11","col-md-12","col-md-2","col-md-3","col-md-4","col-md-5","col-md-6","col-md-7","col-md-8","col-md-9","col-md-auto","col-sm","col-sm-1","col-sm-10","col-sm-11","col-sm-12","col-sm-2","col-sm-3","col-sm-4","col-sm-5","col-sm-6","col-sm-7","col-sm-8","col-sm-9","col-sm-auto","col-xl","col-xl-1","col-xl-10","col-xl-11","col-xl-12","col-xl-2","col-xl-3","col-xl-4","col-xl-5","col-xl-6","col-xl-7","col-xl-8","col-xl-9","col-xl-auto","collapse","collapsing","container","container-fluid","container-lg","container-md","container-sm","container-xl","custom-checkbox","custom-control","custom-control-inline","custom-control-input","custom-control-label","custom-file","custom-file-input","custom-file-label","custom-radio","custom-range","custom-select","custom-select-lg","custom-select-sm","custom-switch","d-block","d-flex","d-inline","d-inline-block","d-inline-flex","d-lg-block","d-lg-flex","d-lg-inline","d-lg-inline-block","d-lg-inline-flex","d-lg-none","d-lg-table","d-lg-table-cell","d-lg-table-row","d-md-block","d-md-flex","d-md-inline","d-md-inline-block","d-md-inline-flex","d-md-none","d-md-table","d-md-table-cell","d-md-table-row","d-none","d-print-block","d-print-flex","d-print-inline","d-print-inline-block","d-print-inline-flex","d-print-none","d-print-table","d-print-table-cell","d-print-table-row","d-sm-block","d-sm-flex","d-sm-inline","d-sm-inline-block","d-sm-inline-flex","d-sm-none","d-sm-table","d-sm-table-cell","d-sm-table-row","d-table","d-table-cell","d-table-row","d-xl-block","d-xl-flex","d-xl-inline","d-xl-inline-block","d-xl-inline-flex","d-xl-none","d-xl-table","d-xl-table-cell","d-xl-table-row","disabled","display-1","display-2","display-3","display-4","dropdown","dropdown-divider","dropdown-header","dropdown-item","dropdown-item-text","dropdown-menu","dropdown-menu-left","dropdown-menu-lg-left","dropdown-menu-lg-right","dropdown-menu-md-left","dropdown-menu-md-right","dropdown-menu-right","dropdown-menu-sm-left","dropdown-menu-sm-right","dropdown-menu-xl-left","dropdown-menu-xl-right","dropdown-toggle","dropdown-toggle-split","dropleft","dropright","dropup","embed-responsive","embed-responsive-16by9","embed-responsive-1by1","embed-responsive-21by9","embed-responsive-4by3","embed-responsive-item","fade","figure","figure-caption","figure-img","fixed-bottom","fixed-top","flex-column","flex-column-reverse","flex-fill","flex-grow-0","flex-grow-1","flex-lg-column","flex-lg-column-reverse","flex-lg-fill","flex-lg-grow-0","flex-lg-grow-1","flex-lg-nowrap","flex-lg-row","flex-lg-row-reverse","flex-lg-shrink-0","flex-lg-shrink-1","flex-lg-wrap","flex-lg-wrap-reverse","flex-md-column","flex-md-column-reverse","flex-md-fill","flex-md-grow-0","flex-md-grow-1","flex-md-nowrap","flex-md-row","flex-md-row-reverse","flex-md-shrink-0","flex-md-shrink-1","flex-md-wrap","flex-md-wrap-reverse","flex-nowrap","flex-row","flex-row-reverse","flex-shrink-0","flex-shrink-1","flex-sm-column","flex-sm-column-reverse","flex-sm-fill","flex-sm-grow-0","flex-sm-grow-1","flex-sm-nowrap","flex-sm-row","flex-sm-row-reverse","flex-sm-shrink-0","flex-sm-shrink-1","flex-sm-wrap","flex-sm-wrap-reverse","flex-wrap","flex-wrap-reverse","flex-xl-column","flex-xl-column-reverse","flex-xl-fill","flex-xl-grow-0","flex-xl-grow-1","flex-xl-nowrap","flex-xl-row","flex-xl-row-reverse","flex-xl-shrink-0","flex-xl-shrink-1","flex-xl-wrap","flex-xl-wrap-reverse","float-left","float-lg-left","float-lg-none","float-lg-right","float-md-left","float-md-none","float-md-right","float-none","float-right","float-sm-left","float-sm-none","float-sm-right","float-xl-left","float-xl-none","float-xl-right","focus","font-italic","font-weight-bold","font-weight-bolder","font-weight-light","font-weight-lighter","font-weight-normal","form-check","form-check-inline","form-check-input","form-check-label","form-control","form-control-file","form-control-lg","form-control-plaintext","form-control-range","form-control-sm","form-group","form-inline","form-row","form-text","h-100","h-25","h-50","h-75","h-auto","h1","h2","h3","h4","h5","h6","hide","img-fluid","img-thumbnail","initialism","input-group","input-group-append","input-group-lg","input-group-prepend","input-group-sm","input-group-text","invalid-feedback","invalid-tooltip","invisible","is-invalid","is-valid","jumbotron","jumbotron-fluid","justify-content-around","justify-content-between","justify-content-center","justify-content-end","justify-content-lg-around","justify-content-lg-between","justify-content-lg-center","justify-content-lg-end","justify-content-lg-start","justify-content-md-around","justify-content-md-between","justify-content-md-center","justify-content-md-end","justify-content-md-start","justify-content-sm-around","justify-content-sm-between","justify-content-sm-center","justify-content-sm-end","justify-content-sm-start","justify-content-start","justify-content-xl-around","justify-content-xl-between","justify-content-xl-center","justify-content-xl-end","justify-content-xl-start","lead","list-group","list-group-flush","list-group-horizontal","list-group-horizontal-lg","list-group-horizontal-md","list-group-horizontal-sm","list-group-horizontal-xl","list-group-item","list-group-item-action","list-group-item-danger","list-group-item-dark","list-group-item-info","list-group-item-light","list-group-item-primary","list-group-item-secondary","list-group-item-success","list-group-item-warning","list-inline","list-inline-item","list-unstyled","m-0","m-1","m-2","m-3","m-4","m-5","m-auto","m-lg-0","m-lg-1","m-lg-2","m-lg-3","m-lg-4","m-lg-5","m-lg-auto","m-lg-n1","m-lg-n2","m-lg-n3","m-lg-n4","m-lg-n5","m-md-0","m-md-1","m-md-2","m-md-3","m-md-4","m-md-5","m-md-auto","m-md-n1","m-md-n2","m-md-n3","m-md-n4","m-md-n5","m-n1","m-n2","m-n3","m-n4","m-n5","m-sm-0","m-sm-1","m-sm-2","m-sm-3","m-sm-4","m-sm-5","m-sm-auto","m-sm-n1","m-sm-n2","m-sm-n3","m-sm-n4","m-sm-n5","m-xl-0","m-xl-1","m-xl-2","m-xl-3","m-xl-4","m-xl-5","m-xl-auto","m-xl-n1","m-xl-n2","m-xl-n3","m-xl-n4","m-xl-n5","mark","mb-0","mb-1","mb-2","mb-3","mb-4","mb-5","mb-auto","mb-lg-0","mb-lg-1","mb-lg-2","mb-lg-3","mb-lg-4","mb-lg-5","mb-lg-auto","mb-lg-n1","mb-lg-n2","mb-lg-n3","mb-lg-n4","mb-lg-n5","mb-md-0","mb-md-1","mb-md-2","mb-md-3","mb-md-4","mb-md-5","mb-md-auto","mb-md-n1","mb-md-n2","mb-md-n3","mb-md-n4","mb-md-n5","mb-n1","mb-n2","mb-n3","mb-n4","mb-n5","mb-sm-0","mb-sm-1","mb-sm-2","mb-sm-3","mb-sm-4","mb-sm-5","mb-sm-auto","mb-sm-n1","mb-sm-n2","mb-sm-n3","mb-sm-n4","mb-sm-n5","mb-xl-0","mb-xl-1","mb-xl-2","mb-xl-3","mb-xl-4","mb-xl-5","mb-xl-auto","mb-xl-n1","mb-xl-n2","mb-xl-n3","mb-xl-n4","mb-xl-n5","media","media-body","mh-100","min-vh-100","min-vw-100","ml-0","ml-1","ml-2","ml-3","ml-4","ml-5","ml-auto","ml-lg-0","ml-lg-1","ml-lg-2","ml-lg-3","ml-lg-4","ml-lg-5","ml-lg-auto","ml-lg-n1","ml-lg-n2","ml-lg-n3","ml-lg-n4","ml-lg-n5","ml-md-0","ml-md-1","ml-md-2","ml-md-3","ml-md-4","ml-md-5","ml-md-auto","ml-md-n1","ml-md-n2","ml-md-n3","ml-md-n4","ml-md-n5","ml-n1","ml-n2","ml-n3","ml-n4","ml-n5","ml-sm-0","ml-sm-1","ml-sm-2","ml-sm-3","ml-sm-4","ml-sm-5","ml-sm-auto","ml-sm-n1","ml-sm-n2","ml-sm-n3","ml-sm-n4","ml-sm-n5","ml-xl-0","ml-xl-1","ml-xl-2","ml-xl-3","ml-xl-4","ml-xl-5","ml-xl-auto","ml-xl-n1","ml-xl-n2","ml-xl-n3","ml-xl-n4","ml-xl-n5","modal","modal-backdrop","modal-body","modal-content","modal-dialog","modal-dialog-centered","modal-dialog-scrollable","modal-footer","modal-header","modal-lg","modal-open","modal-scrollbar-measure","modal-sm","modal-static","modal-title","modal-xl","mr-0","mr-1","mr-2","mr-3","mr-4","mr-5","mr-auto","mr-lg-0","mr-lg-1","mr-lg-2","mr-lg-3","mr-lg-4","mr-lg-5","mr-lg-auto","mr-lg-n1","mr-lg-n2","mr-lg-n3","mr-lg-n4","mr-lg-n5","mr-md-0","mr-md-1","mr-md-2","mr-md-3","mr-md-4","mr-md-5","mr-md-auto","mr-md-n1","mr-md-n2","mr-md-n3","mr-md-n4","mr-md-n5","mr-n1","mr-n2","mr-n3","mr-n4","mr-n5","mr-sm-0","mr-sm-1","mr-sm-2","mr-sm-3","mr-sm-4","mr-sm-5","mr-sm-auto","mr-sm-n1","mr-sm-n2","mr-sm-n3","mr-sm-n4","mr-sm-n5","mr-xl-0","mr-xl-1","mr-xl-2","mr-xl-3","mr-xl-4","mr-xl-5","mr-xl-auto","mr-xl-n1","mr-xl-n2","mr-xl-n3","mr-xl-n4","mr-xl-n5","mt-0","mt-1","mt-2","mt-3","mt-4","mt-5","mt-auto","mt-lg-0","mt-lg-1","mt-lg-2","mt-lg-3","mt-lg-4","mt-lg-5","mt-lg-auto","mt-lg-n1","mt-lg-n2","mt-lg-n3","mt-lg-n4","mt-lg-n5","mt-md-0","mt-md-1","mt-md-2","mt-md-3","mt-md-4","mt-md-5","mt-md-auto","mt-md-n1","mt-md-n2","mt-md-n3","mt-md-n4","mt-md-n5","mt-n1","mt-n2","mt-n3","mt-n4","mt-n5","mt-sm-0","mt-sm-1","mt-sm-2","mt-sm-3","mt-sm-4","mt-sm-5","mt-sm-auto","mt-sm-n1","mt-sm-n2","mt-sm-n3","mt-sm-n4","mt-sm-n5","mt-xl-0","mt-xl-1","mt-xl-2","mt-xl-3","mt-xl-4","mt-xl-5","mt-xl-auto","mt-xl-n1","mt-xl-n2","mt-xl-n3","mt-xl-n4","mt-xl-n5","mw-100","mx-0","mx-1","mx-2","mx-3","mx-4","mx-5","mx-auto","mx-lg-0","mx-lg-1","mx-lg-2","mx-lg-3","mx-lg-4","mx-lg-5","mx-lg-auto","mx-lg-n1","mx-lg-n2","mx-lg-n3","mx-lg-n4","mx-lg-n5","mx-md-0","mx-md-1","mx-md-2","mx-md-3","mx-md-4","mx-md-5","mx-md-auto","mx-md-n1","mx-md-n2","mx-md-n3","mx-md-n4","mx-md-n5","mx-n1","mx-n2","mx-n3","mx-n4","mx-n5","mx-sm-0","mx-sm-1","mx-sm-2","mx-sm-3","mx-sm-4","mx-sm-5","mx-sm-auto","mx-sm-n1","mx-sm-n2","mx-sm-n3","mx-sm-n4","mx-sm-n5","mx-xl-0","mx-xl-1","mx-xl-2","mx-xl-3","mx-xl-4","mx-xl-5","mx-xl-auto","mx-xl-n1","mx-xl-n2","mx-xl-n3","mx-xl-n4","mx-xl-n5","my-0","my-1","my-2","my-3","my-4","my-5","my-auto","my-lg-0","my-lg-1","my-lg-2","my-lg-3","my-lg-4","my-lg-5","my-lg-auto","my-lg-n1","my-lg-n2","my-lg-n3","my-lg-n4","my-lg-n5","my-md-0","my-md-1","my-md-2","my-md-3","my-md-4","my-md-5","my-md-auto","my-md-n1","my-md-n2","my-md-n3","my-md-n4","my-md-n5","my-n1","my-n2","my-n3","my-n4","my-n5","my-sm-0","my-sm-1","my-sm-2","my-sm-3","my-sm-4","my-sm-5","my-sm-auto","my-sm-n1","my-sm-n2","my-sm-n3","my-sm-n4","my-sm-n5","my-xl-0","my-xl-1","my-xl-2","my-xl-3","my-xl-4","my-xl-5","my-xl-auto","my-xl-n1","my-xl-n2","my-xl-n3","my-xl-n4","my-xl-n5","nav","nav-fill","nav-item","nav-justified","nav-link","nav-pills","nav-tabs","navbar","navbar-brand","navbar-collapse","navbar-dark","navbar-expand","navbar-expand-lg","navbar-expand-md","navbar-expand-sm","navbar-expand-xl","navbar-light","navbar-nav","navbar-text","navbar-toggler","navbar-toggler-icon","no-gutters","offset-1","offset-10","offset-11","offset-2","offset-3","offset-4","offset-5","offset-6","offset-7","offset-8","offset-9","offset-lg-0","offset-lg-1","offset-lg-10","offset-lg-11","offset-lg-2","offset-lg-3","offset-lg-4","offset-lg-5","offset-lg-6","offset-lg-7","offset-lg-8","offset-lg-9","offset-md-0","offset-md-1","offset-md-10","offset-md-11","offset-md-2","offset-md-3","offset-md-4","offset-md-5","offset-md-6","offset-md-7","offset-md-8","offset-md-9","offset-sm-0","offset-sm-1","offset-sm-10","offset-sm-11","offset-sm-2","offset-sm-3","offset-sm-4","offset-sm-5","offset-sm-6","offset-sm-7","offset-sm-8","offset-sm-9","offset-xl-0","offset-xl-1","offset-xl-10","offset-xl-11","offset-xl-2","offset-xl-3","offset-xl-4","offset-xl-5","offset-xl-6","offset-xl-7","offset-xl-8","offset-xl-9","order-0","order-1","order-10","order-11","order-12","order-2","order-3","order-4","order-5","order-6","order-7","order-8","order-9","order-first","order-last","order-lg-0","order-lg-1","order-lg-10","order-lg-11","order-lg-12","order-lg-2","order-lg-3","order-lg-4","order-lg-5","order-lg-6","order-lg-7","order-lg-8","order-lg-9","order-lg-first","order-lg-last","order-md-0","order-md-1","order-md-10","order-md-11","order-md-12","order-md-2","order-md-3","order-md-4","order-md-5","order-md-6","order-md-7","order-md-8","order-md-9","order-md-first","order-md-last","order-sm-0","order-sm-1","order-sm-10","order-sm-11","order-sm-12","order-sm-2","order-sm-3","order-sm-4","order-sm-5","order-sm-6","order-sm-7","order-sm-8","order-sm-9","order-sm-first","order-sm-last","order-xl-0","order-xl-1","order-xl-10","order-xl-11","order-xl-12","order-xl-2","order-xl-3","order-xl-4","order-xl-5","order-xl-6","order-xl-7","order-xl-8","order-xl-9","order-xl-first","order-xl-last","overflow-auto","overflow-hidden","p-0","p-1","p-2","p-3","p-4","p-5","p-lg-0","p-lg-1","p-lg-2","p-lg-3","p-lg-4","p-lg-5","p-md-0","p-md-1","p-md-2","p-md-3","p-md-4","p-md-5","p-sm-0","p-sm-1","p-sm-2","p-sm-3","p-sm-4","p-sm-5","p-xl-0","p-xl-1","p-xl-2","p-xl-3","p-xl-4","p-xl-5","page-item","page-link","pagination","pagination-lg","pagination-sm","pb-0","pb-1","pb-2","pb-3","pb-4","pb-5","pb-lg-0","pb-lg-1","pb-lg-2","pb-lg-3","pb-lg-4","pb-lg-5","pb-md-0","pb-md-1","pb-md-2","pb-md-3","pb-md-4","pb-md-5","pb-sm-0","pb-sm-1","pb-sm-2","pb-sm-3","pb-sm-4","pb-sm-5","pb-xl-0","pb-xl-1","pb-xl-2","pb-xl-3","pb-xl-4","pb-xl-5","pl-0","pl-1","pl-2","pl-3","pl-4","pl-5","pl-lg-0","pl-lg-1","pl-lg-2","pl-lg-3","pl-lg-4","pl-lg-5","pl-md-0","pl-md-1","pl-md-2","pl-md-3","pl-md-4","pl-md-5","pl-sm-0","pl-sm-1","pl-sm-2","pl-sm-3","pl-sm-4","pl-sm-5","pl-xl-0","pl-xl-1","pl-xl-2","pl-xl-3","pl-xl-4","pl-xl-5","pointer-event","popover","popover-body","popover-header","position-absolute","position-fixed","position-relative","position-static","position-sticky","pr-0","pr-1","pr-2","pr-3","pr-4","pr-5","pr-lg-0","pr-lg-1","pr-lg-2","pr-lg-3","pr-lg-4","pr-lg-5","pr-md-0","pr-md-1","pr-md-2","pr-md-3","pr-md-4","pr-md-5","pr-sm-0","pr-sm-1","pr-sm-2","pr-sm-3","pr-sm-4","pr-sm-5","pr-xl-0","pr-xl-1","pr-xl-2","pr-xl-3","pr-xl-4","pr-xl-5","pre-scrollable","progress","progress-bar","progress-bar-animated","progress-bar-striped","pt-0","pt-1","pt-2","pt-3","pt-4","pt-5","pt-lg-0","pt-lg-1","pt-lg-2","pt-lg-3","pt-lg-4","pt-lg-5","pt-md-0","pt-md-1","pt-md-2","pt-md-3","pt-md-4","pt-md-5","pt-sm-0","pt-sm-1","pt-sm-2","pt-sm-3","pt-sm-4","pt-sm-5","pt-xl-0","pt-xl-1","pt-xl-2","pt-xl-3","pt-xl-4","pt-xl-5","px-0","px-1","px-2","px-3","px-4","px-5","px-lg-0","px-lg-1","px-lg-2","px-lg-3","px-lg-4","px-lg-5","px-md-0","px-md-1","px-md-2","px-md-3","px-md-4","px-md-5","px-sm-0","px-sm-1","px-sm-2","px-sm-3","px-sm-4","px-sm-5","px-xl-0","px-xl-1","px-xl-2","px-xl-3","px-xl-4","px-xl-5","py-0","py-1","py-2","py-3","py-4","py-5","py-lg-0","py-lg-1","py-lg-2","py-lg-3","py-lg-4","py-lg-5","py-md-0","py-md-1","py-md-2","py-md-3","py-md-4","py-md-5","py-sm-0","py-sm-1","py-sm-2","py-sm-3","py-sm-4","py-sm-5","py-xl-0","py-xl-1","py-xl-2","py-xl-3","py-xl-4","py-xl-5","rounded","rounded-0","rounded-bottom","rounded-circle","rounded-left","rounded-lg","rounded-pill","rounded-right","rounded-sm","rounded-top","row","row-cols-1","row-cols-2","row-cols-3","row-cols-4","row-cols-5","row-cols-6","row-cols-lg-1","row-cols-lg-2","row-cols-lg-3","row-cols-lg-4","row-cols-lg-5","row-cols-lg-6","row-cols-md-1","row-cols-md-2","row-cols-md-3","row-cols-md-4","row-cols-md-5","row-cols-md-6","row-cols-sm-1","row-cols-sm-2","row-cols-sm-3","row-cols-sm-4","row-cols-sm-5","row-cols-sm-6","row-cols-xl-1","row-cols-xl-2","row-cols-xl-3","row-cols-xl-4","row-cols-xl-5","row-cols-xl-6","shadow","shadow-lg","shadow-none","shadow-sm","show","showing","small","spinner-border","spinner-border-sm","spinner-grow","spinner-grow-sm","sr-only","sr-only-focusable","sticky-top","stretched-link","tab-content","table","table-active","table-bordered","table-borderless","table-danger","table-dark","table-hover","table-info","table-light","table-primary","table-responsive","table-responsive-lg","table-responsive-md","table-responsive-sm","table-responsive-xl","table-secondary","table-sm","table-striped","table-success","table-warning","text-black-50","text-body","text-break","text-capitalize","text-center","text-danger","text-dark","text-decoration-none","text-hide","text-info","text-justify","text-left","text-lg-center","text-lg-left","text-lg-right","text-light","text-lowercase","text-md-center","text-md-left","text-md-right","text-monospace","text-muted","text-nowrap","text-primary","text-reset","text-right","text-secondary","text-sm-center","text-sm-left","text-sm-right","text-success","text-truncate","text-uppercase","text-warning","text-white","text-white-50","text-wrap","text-xl-center","text-xl-left","text-xl-right","thead-dark","thead-light","toast","toast-body","toast-header","tooltip","tooltip-inner","valid-feedback","valid-tooltip","vh-100","visible","vw-100","w-100","w-25","w-50","w-75","w-auto","was-validated"]

class Bootstrap43Completions(sublime_plugin.EventListener):
   
    def __init__(self):

        self.class_completions = [("%s \tBootstrap 4.4" % s, s) for s in bootstrap_441_classes]

    def on_query_completions(self, view, prefix, locations):

        if view.match_selector(locations[0], "text.html string.quoted"):


            LIMIT  = 250

            cursor = locations[0] - len(prefix) - 1

            start  = max(0, cursor - LIMIT - len(prefix))

            line   = view.substr(sublime.Region(start, cursor))

            parts  = line.split('=')

            if len(parts) > 1 and parts[-2].strip().endswith("class"):
                return self.class_completions
            else:
                return []
        elif view.match_selector(locations[0], "text.html meta.tag - text.html punctuation.definition.tag.begin"):

            return self.data_completions

        else:

            return []
