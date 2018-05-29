@spotdyna-104 @spotdyna-104 @sanity

Feature: Procesado de trama una vez descargada una nueva lista de reproduccion
	
Scenario: bla bla
  Given un dispositivo final ha finalizado una descarga de una lista de reproducción de contenidos
  When se envia una trama de PUBLICIDAD
  Then Los datos son almacenados en la Base de Datos en la tabla de logs
  And Se obtiene un ACK MQTT de QoS 1
