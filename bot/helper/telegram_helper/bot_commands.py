#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start2'
        self.MirrorCommand = [f'mirror2{CMD_SUFFIX}', f'm2{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror2{CMD_SUFFIX}', f'qm2{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl2{CMD_SUFFIX}', f'y2{CMD_SUFFIX}']
        self.LeechCommand = [f'leech2{CMD_SUFFIX}', f'l2{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech2{CMD_SUFFIX}', f'ql2{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech2{CMD_SUFFIX}', f'yl2{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'unzipmirror2{CMD_SUFFIX}', f'uzm2{CMD_SUFFIX}', f'zipmirror2{CMD_SUFFIX}', f'zm2{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbunzipmirror2{CMD_SUFFIX}', f'quzm2{CMD_SUFFIX}', f'qbzipmirror2{CMD_SUFFIX}', f'qzm2{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'ytdlzip2{CMD_SUFFIX}', f'yz2{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'unzipleech2{CMD_SUFFIX}', f'uzl2{CMD_SUFFIX}', f'zipleech2{CMD_SUFFIX}', f'zl2{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbunzipleech2{CMD_SUFFIX}', f'quzl2{CMD_SUFFIX}', f'qbzipleech2{CMD_SUFFIX}', f'qzl2{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'ytdlzipleech2{CMD_SUFFIX}', f'yzl2{CMD_SUFFIX}'])
        self.CloneCommand = [f'clone2{CMD_SUFFIX}', f'c2{CMD_SUFFIX}']
        self.CountCommand = f'count2{CMD_SUFFIX}'
        self.DeleteCommand = f'del2{CMD_SUFFIX}'
        self.CancelMirror = f'cancel2{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelall2{CMD_SUFFIX}', 'cancellallbot2']
        self.ListCommand = f'list2{CMD_SUFFIX}'
        self.SearchCommand = f'search2{CMD_SUFFIX}'
        self.StatusCommand = [f'status{CMD_SUFFIX}', f's{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize{CMD_SUFFIX}', f'a{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize{CMD_SUFFIX}', f'ua{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'ping{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'restart{CMD_SUFFIX}', f'r{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats{CMD_SUFFIX}', f'st{CMD_SUFFIX}']
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsetting{CMD_SUFFIX}', f'bs{CMD_SUFFIX}']
        self.UserSetCommand = [f'usetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest{CMD_SUFFIX}', f'sp{CMD_SUFFIX}']
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb{CMD_SUFFIX}'
        self.AniListCommand = f'anime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfo{CMD_SUFFIX}', f'mi{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdclean{CMD_SUFFIX}', f'gc{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcast{CMD_SUFFIX}', f'bc{CMD_SUFFIX}']

BotCommands = _BotCommands()
