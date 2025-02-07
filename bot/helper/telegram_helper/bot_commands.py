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
        self.CancelAllCommand = [f'cancelall2{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'list2{CMD_SUFFIX}'
        self.SearchCommand = f'search2{CMD_SUFFIX}'
        self.StatusCommand = [f'status2{CMD_SUFFIX}', f's2{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users2{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize2{CMD_SUFFIX}', f'a2{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize2{CMD_SUFFIX}', f'ua2{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist2{CMD_SUFFIX}', f'bl2{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist2{CMD_SUFFIX}', f'rbl2{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo2{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo2{CMD_SUFFIX}'
        self.PingCommand = [f'ping{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'restart{CMD_SUFFIX}', f'r{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats2{CMD_SUFFIX}', f'st2{CMD_SUFFIX}']
        self.HelpCommand = f'help2{CMD_SUFFIX}'
        self.LogCommand = f'log2{CMD_SUFFIX}'
        self.ShellCommand = f'shell2{CMD_SUFFIX}'
        self.EvalCommand = f'eval2{CMD_SUFFIX}'
        self.ExecCommand = f'exec2{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals2{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsetting2{CMD_SUFFIX}', f'bs2{CMD_SUFFIX}']
        self.UserSetCommand = [f'usetting2{CMD_SUFFIX}', f'us2{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel2{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel2{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest2{CMD_SUFFIX}', f'sp2{CMD_SUFFIX}']
        self.RssCommand = f'rss2{CMD_SUFFIX}'
        self.LoginCommand = 'login2'
        self.AddImageCommand = f'addimg2{CMD_SUFFIX}'
        self.ImagesCommand = f'images2{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb2{CMD_SUFFIX}'
        self.AniListCommand = f'anime2{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp2{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfo2{CMD_SUFFIX}', f'mi2{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl2{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdclean2{CMD_SUFFIX}', f'gc2{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcast2{CMD_SUFFIX}', f'bc2{CMD_SUFFIX}']

BotCommands = _BotCommands()
