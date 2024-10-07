from django.urls import path
from components.views import (
    
    # forms
    forms_elements_view,
    forms_validation_view,
    forms_advanced_view,
    forms_editors_view,
    forms_file_uploads_view,
    forms_wizard_view,
    forms_mask_view,
    
    # tables
    tables_basic_view,
    tables_advanced_view,
    
    # apex-charts
    apexcharts_line_view,
    apexcharts_area_view,
    apexcharts_column_view,
    apexcharts_bar_view,
    apexcharts_mixed_view,
    apexcharts_timeline_view,
    apexcharts_candlestick_view,
    apexcharts_boxplot_view,
    apexcharts_bubble_view,
    apexcharts_scatter_view,
    apexcharts_heatmap_view,
    apexcharts_treemap_view,
    apexcharts_pie_view,
    apexcharts_radialbar_view,
    apexcharts_radar_view,
    apexcharts_polararea_view,
    
    # icons
    icons_unicons_view,
    icons_feathericons_view,
    icons_boxicons_view,
    icons_materialdesign_view,
    icons_fontawesome_view,
    
    # maps
    maps_google_view,
    maps_vector_view,
    maps_leaflet_view,
    
    
    
)

app_name = "components"

urlpatterns = [
    
    path('forms/elements',view=forms_elements_view,name="forms.elements"),
    path('forms/validation',view=forms_validation_view,name="forms.validation"),
    path('forms/advanced',view=forms_advanced_view,name="forms.advanced"),
    path('forms/editors',view=forms_editors_view,name="forms.editors"),
    path('forms/file_uploads',view=forms_file_uploads_view,name="forms.file_uploads"),
    path('forms/wizard',view=forms_wizard_view,name="forms.wizard"),
    path('forms/mask',view=forms_mask_view,name="forms.mask"),
    
    # tables
    path('tables/basic',view=tables_basic_view,name="tables.basic"),
    path('tables/advanced',view=tables_advanced_view,name="tables.advanced"),
    
    # apex-charts
    path('apex-charts/line',view=apexcharts_line_view,name="apex-charts.line"),
    path('apex-charts/area',view=apexcharts_area_view,name="apex-charts.area"),
    path('apex-charts/column',view=apexcharts_column_view,name="apex-charts.column"),
    path('apex-charts/bar',view=apexcharts_bar_view,name="apex-charts.bar"),
    path('apex-charts/mixed',view=apexcharts_mixed_view,name="apex-charts.mixed"),
    path('apex-charts/timeline',view=apexcharts_timeline_view,name="apex-charts.timeline"),
    path('apex-charts/candlestick',view=apexcharts_candlestick_view,name="apex-charts.candlestick"),
    path('apex-charts/boxplot',view=apexcharts_boxplot_view,name="apex-charts.boxplot"),
    path('apex-charts/bubble',view=apexcharts_bubble_view,name="apex-charts.bubble"),
    path('apex-charts/scatter',view=apexcharts_scatter_view,name="apex-charts.scatter"),
    path('apex-charts/heatmap',view=apexcharts_heatmap_view,name="apex-charts.heatmap"),
    path('apex-charts/treemap',view=apexcharts_treemap_view,name="apex-charts.treemap"),
    path('apex-charts/pie',view=apexcharts_pie_view,name="apex-charts.pie"),
    path('apex-charts/radialbar',view=apexcharts_radialbar_view,name="apex-charts.radialbar"),
    path('apex-charts/radar',view=apexcharts_radar_view,name="apex-charts.radar"),
    path('apex-charts/polararea',view=apexcharts_polararea_view,name="apex-charts.polararea"),

    # icons
    path('icons/unicons',view=icons_unicons_view,name="icons.unicons"),
    path('icons/feathericons',view=icons_feathericons_view,name="icons.feathericons"),
    path('icons/boxicons',view=icons_boxicons_view,name="icons.boxicons"),
    path('icons/materialdesign',view=icons_materialdesign_view,name="icons.materialdesign"),
    path('icons/fontawesome',view=icons_fontawesome_view,name="icons.fontawesome"),
    
    # maps
    path('maps/google',view=maps_google_view,name="maps.google"),
    path('maps/vector',view=maps_vector_view,name="maps.vector"),
    path('maps/leaflet',view=maps_leaflet_view,name="maps.leaflet"),
    

    
    
]
