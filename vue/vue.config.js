const BundleTracker = require('webpack-bundle-tracker');

/*
This is required for the static directory below
const path = require('path');

function resolve(dir) {
    return path.join(__dirname, dir);
}
*/

const pages = {
    example: {
        entry: './src/example.js',
        chunks: ['chunk-vendors'],
    },
};

module.exports = {
    pages,
    filenameHashing: false,
    productionSourceMap: false,
    publicPath: process.env.NODE_ENV === 'production'
        ? '../'
        : 'http://localhost:8080/',
    outputDir: '../vue_built/vue/',
    assetsDir: process.env.NODE_ENV === 'production'
        ? '../static/vue/'
        : '',

    chainWebpack: (config) => {
        config.optimization
            .splitChunks({
                cacheGroups: {
                    vendor: {
                        test: /[\\/]node_modules[\\/]/,
                        name: 'chunk-vendors',
                        chunks: 'all',
                        priority: 1,
                    },
                },
            });

        Object.keys(pages).forEach((page) => {
            config.plugins.delete(`html-${page}`);
            config.plugins.delete(`preload-${page}`);
            config.plugins.delete(`prefetch-${page}`);
        });

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{ filename: '../vue/webpack-stats.json' }]);

        // Below can be used to have an additional static directory
        // config.resolve.alias
        //   .set('__STATIC__', resolve('../vue_static'));

        config.devServer
            .public('http://localhost:8080')
            .host('localhost')
            .port(8080)
            .hotOnly(true)
            .watchOptions({ poll: 1000 })
            .https(false)
            .headers({ 'Access-Control-Allow-Origin': ['*'] });
    },
};
