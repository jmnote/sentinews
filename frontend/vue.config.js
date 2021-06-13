module.exports = {
    devServer: {
      disableHostCheck: true,
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