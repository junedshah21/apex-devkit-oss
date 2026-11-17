-- Original synthetic input for APEX DevKit OSS.
-- Illustrative declarations only. This is NOT an installable Oracle APEX export.
begin
  wwv_flow_imp_page.create_page(p_id => 1);
  wwv_flow_imp_page.create_page_plug(p_id => 2);
  wwv_flow_imp_page.create_report_region(p_id => 3);
  wwv_flow_imp_page.create_page_item(p_id => 4);
  wwv_flow_imp_page.create_page_button(p_id => 5);
  wwv_flow_imp_page.create_page_da_event(p_id => 6);
  wwv_flow_imp_page.create_page_process(p_id => 7);
  wwv_flow_imp_shared.create_list_of_values(p_id => 8);
end;
/
