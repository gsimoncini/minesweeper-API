def main():
    import argparse
    parser = argparse.ArgumentParser(epilog=__doc__)
    parser.add_argument('--env', action='store', default='development',
                        help='mode in which the app should run: sandbox, dev or production')
    parser.add_argument('--port', type=int, default=5001, help='port to run on when in local mode')
    args = parser.parse_args()

    print('Running as "{env}"'.format(env=args.env))

    from app import app

    print('Flask API is running on %s mode, go play with it =)' % args.env)
    app.run(
        host='0.0.0.0',
        port=args.port,
        debug=True,
        threaded=True)

if __name__ == '__main__':
    main()
