-- EXAMPLE ONLY. Paste into an authorized APEX application Ajax Callback process.
-- Requires APEX_JSON and an authenticated user; add your application's authorization scheme.
-- This makes no database modifications; returns the calling username.
-- Avoid exposing account details or accepting client-supplied identity.
BEGIN
  IF :APP_USER IS NULL OR :APP_USER IN ('nobody', 'APEX_PUBLIC_USER') THEN
    raise_application_error(-20001, 'Authentication required');
  END IF;
  apex_json.open_object;
  apex_json.write('success', TRUE);
  apex_json.write('user', :APP_USER);
  apex_json.close_object;
END;
/
