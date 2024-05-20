import { KeycloakService } from 'keycloak-angular';
import { KeycloakConfig } from 'keycloak-js';

function initializeKeycloak(keycloak: KeycloakService) {
  const keycloakConfig: KeycloakConfig = {
    url: 'http://localhost:8180/',
    realm: 'srifin',
    clientId: 'srifin_client',
    
  };

  return () =>
    keycloak.init({
      config: keycloakConfig,
      initOptions: {
        onLoad: 'login-required',
        checkLoginIframe: false
      }
    }).catch((error) => {
        console.error('Keycloak initialization failed:', error);
        // Handle the initialization error
        alert('Failed to initialize authentication service.');
    });
}

export { initializeKeycloak };
