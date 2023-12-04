<?php
/**
 * Функции и определения темы "ip"
 *
 * @link https://developer.wordpress.org/themes/basics/theme-functions/
 *
 * @package ip
 */

// Подключение кастомных шрифтов
function custom_fonts() {
    wp_enqueue_style('custom-fonts', get_template_directory_uri() . '/fonts.css');
}
add_action('wp_enqueue_scripts', 'custom_fonts');

if ( ! defined( '_S_VERSION' ) ) {
    // Замените номер версии темы при каждом релизе.
    define( '_S_VERSION', '1.0.8' );
}

if ( ! function_exists( 'ip_setup' ) ) :
    /**
     * Настройка темы по умолчанию и регистрация поддержки различных функций WordPress.
     */
    function ip_setup() {
        load_theme_textdomain( 'ip', get_template_directory() . '/languages' );

        // Поддержка автоматических ссылок на RSS каналы для записей и комментариев.
        add_theme_support( 'automatic-feed-links' );

        // Позволяет WordPress управлять заголовком документа.
        add_theme_support( 'title-tag' );

        // Включение поддержки миниатюр для записей и страниц.
        add_theme_support( 'post-thumbnails' );

        // Включение краткого описания для страниц.
        add_post_type_support( 'page', array('excerpt') );

        // Регистрация одного меню навигации.
        register_nav_menus(
            array(
                'menu-1'    => esc_html__( 'Главное меню', 'ip' ),
                'footer-1'  => esc_html__( 'Footer 1', 'ip' ),
                'footer-2'  => esc_html__( 'Footer 2', 'ip' ),
            )
        );

        // Переключение ядра WordPress на вывод действительного HTML5.
        add_theme_support(
            'html5',
            array(
                'search-form',
                'comment-form',
                'comment-list',
                'gallery',
                'caption',
                'style',
                'script',
            )
        );

        // Настройка фона темы WordPress.
        add_theme_support(
            'custom-background',
            apply_filters(
                'ip_custom_background_args',
                array(
                    'default-color' => 'ffffff',
                    'default-image' => '',
                )
            )
        );

        // Поддержка выборочного обновления виджетов для настройки.
        add_theme_support( 'customize-selective-refresh-widgets' );

        /**
         * Добавление поддержки кастомного логотипа.
         *
         * @link https://codex.wordpress.org/Theme_Logo
         */
        add_theme_support(
            'custom-logo',
            array(
                'height'      => 73,
                'width'       => 222,
                'flex-width'  => true,
                'flex-height' => true,
            )
        );
    }
endif;
add_action( 'after_setup_theme', 'ip_setup' );

/**
 * Задает ширину контента в пикселях, основываясь на дизайне темы и таблице стилей.
 *
 * Приоритет 0, чтобы сделать его доступным для функций с более низким приоритетом.
 *
 * @global int $content_width
 */
function ip_content_width() {
    $GLOBALS['content_width'] = apply_filters( 'ip_content_width', 640 );
}
add_action( 'after_setup_theme', 'ip_content_width', 0 );

/**
 * Регистрация области виджетов.
 */
function ip_widgets_init() {
    register_sidebar(
        array(
            'name'          => esc_html__( 'Sidebar', 'ip' ),
            'id'            => 'sidebar-1',
            'description'   => esc_html__( 'Добавьте сюда виджеты.', 'ip' ),
            'before_widget' => '<section id="%1$s" class="widget %2$s">',
            'after_widget'  => '</section>',
            'before_title'  => '<h2 class="widget-title">',
            'after_title'   => '</h2>',
        )
    );
}
add_action( 'widgets_init', 'ip_widgets_init' );

/**
 * Подключение скриптов и стилей.
 */
function add_svg_to_upload_mimes($upload_mimes) {
    $upload_mimes['svg'] = 'image/svg+xml';
    return $upload_mimes;
}
add_filter('upload_mimes', 'add_svg_to_upload_mimes');

if ( is_home() ) {
    wp_enqueue_script( 'scroll-js', get_template_directory_uri() . '/scroll.js', array('jquery'), _S_VERSION, true );
}
function ip_scripts() {
    wp_enqueue_style( 'ip-style', get_stylesheet_uri(), array('js_composer_front', 'wpc-filter-everything'), _S_VERSION );
    wp_register_script( 'slick', get_template_directory_uri() . '/js/slick.min.js', array('jquery'), '1.9.0', true );
    wp_enqueue_script( 'slick' );
    wp_enqueue_script( 'jquery-inputmask', get_template_directory_uri() . '/js/jquery.inputmask.bundle.js', array('jquery'), '4', true );
    wp_enqueue_script( 'magnific-popup-js', get_template_directory_uri() . '/js/jquery.magnific-popup.js', array('jquery'), '', true );
    wp_enqueue_script( 'ip-navigation', get_template_directory_uri() . '/js/navigation.js', array(), _S_VERSION, true );
    wp_enqueue_script( 'blocks', get_template_directory_uri() . '/js/blocks.js', array('jquery'), _S_VERSION, true );
    wp_enqueue_script( 'main-js', get_template_directory_uri() . '/js/main.js', array('jquery'), _S_VERSION, true );
    wp_register_script( 'api-maps-yandex', 'https://api-maps.yandex.ru/2.1/?lang=ru_RU', array('jquery'), '', true );
}
add_action( 'wp_enqueue_scripts', 'ip_scripts' );

// Реализация кастомного заголовка.
require get_template_directory() . '/' . 'inc/custom-header.php';

// Пользовательские метки для темы.
require get_template_directory() . '/' . 'inc/template-tags.php';

// Функции, улучшающие тему, подключение через хуки WordPress.
require get_template_directory() . '/' . 'inc/template-functions.php';

// Дополнения для настройки темы.
require get_template_directory() . '/' . 'inc/customizer.php';

// Загрузка совместимости с Jetpack.
if ( defined( 'JETPACK__VERSION' ) ) {
    require get_template_directory() . '/' . 'inc/jetpack.php';
}

// Загрузка совместимости с WooCommerce.
if ( class_exists( 'WooCommerce' ) ) {
    require get_template_directory() . '/' . 'inc/woocommerce.php';
}

// Настройки темы.
require get_template_directory() . '/' . 'inc/options.php';

// Блоки для WPBakery Page Builder
// и другие блоки
require get_template_directory() . '/' . 'inc/wpb_blocks.php';

// SEO
require get_template_directory() . '/' . 'inc/seo.php';
