module.exports = {
    devServer: {
      disableHostCheck: true,
      port: 9000,
    },
  
    transpileDependencies: ['vuetify'],
  
    pluginOptions: {
      i18n: {
        locale: 'ko',
        fallbackLocale: 'en',
        localeDir: 'locales',
        enableInSFC: false,
      },
    },
  }