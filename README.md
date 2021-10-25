# Trabajo 3: Segmentación de clientes

Una empresa de tarjetas de crédito ha monitorizado los movimientos realizados por algunos de sus clientes durante los últimos 6 meses. Esta información la ha resumido y la ha agregado a un fichero de datos con el fin de encontrar patrones en dichos clientes.

Esta empresa os pide:

editado por cris

* Realizar un análisis exploratorio de los datos detallando aquellos aspectos más relevantes que hayáis encontrado.
* Montar un modelo de clustering para segmentar los clientes en función de su comportamiento de compras.
* Desarrollar un cuadro de mando con dash donde podamos observar los aspectos más relevantes que hayáis obtenido en el descriptivo y pueda agrupar nuevos clientes en un cluster determinado.

¿Qué recomendaciones le haríais a la empresa para mantener o mejorar la experiencia del cliente?

## Información de los datos:

* CUSTID : Identificador de cliente
* BALANCE : Saldo restante en su cuenta para hacer compras
* BALANCEFREQUENCY : Frecuencia con la que el saldo es actualizado. Valor entre 0 y 1 (1 = Frecuencia alta, 0 = Frecuencia baja)
* PURCHASES : Pagos por compras hechas desde la cuenta
* ONEOFFPURCHASES : Cantidad máxima hecha en una compra.
* INSTALLMENTSPURCHASES : Cantidad de compra pagada a plazos.
* CASHADVANCE : Pagos en efectivo por adelantado dado por el cliente.
* PURCHASESFREQUENCY : Como de frecuentes son los pagos realizados por el cliente. Valor entre 0 y 1 (1 = Alta frecuencia, 0 = Baja frecuencia)
* ONEOFFPURCHASESFREQUENCY : Con que frecuencia se realizan las compras de pagadas en una vez. Valor entre 0 y 1 (1 = Alta frecuencia, 0 = Baja frecuencia)
* PURCHASESINSTALLMENTSFREQUENCY : Con que frecuencia se realizan los pagos a plazos. Valor entre 0 y 1 (1 = Alta frecuencia, 0 = Baja frecuencia)
* CASHADVANCEFREQUENCY : Frecuencia de pagos en efectivo por adelantado. Valor entre 0 y 1 (1 = Alta frecuencia, 0 = Baja frecuencia)
* CASHADVANCETRX : Número de transacciones realizadas mediantes pagos en efectivo por adelantado.
* PURCHASESTRX : Número de transacciones de compras realizadas desde la cuenta
* CREDITLIMIT : Límite de la tarjeta de crédito
* PAYMENTS : Dinero total pagado por el cliente
* MINIMUM_PAYMENTS : Cantidad mínima entre los pagos realizados por el cliente.
* PRCFULLPAYMENT : Porcentaje del pago total realizado por el cliente
* TENURE : Permanencia de la tarjeta de crédito.
