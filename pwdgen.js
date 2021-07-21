var hotpOtpGenerator = require('hotp-totp-generator')

   // Example of TOTP
  const totpToken = hotpOtpGenerator.totp({ key: 'temirlan.zhekenov@nu.edu.kzDPSCHALLENGE', algorithm: 'sha512',X: '120',T0: '0',digits: '10'});
  
  console.log(totpToken)