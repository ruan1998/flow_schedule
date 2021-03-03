# from pprint import pprint
import json

node_info = {'节点':
    [
        {'ID':["ID名", "ID编号"]},
        {"属性":["职级", "处理能力", "处理用时", "概率"]},
        {'功能':[
            {"基本功能":[
                {"业务功能": ["性息通信", "流程处理", "知识推理"]},
                {"管理功能": ["任务调度"]}
            ]},
            {"学习功能": ["基本功能学习", "学习新能力"]}
        ]},
        {"状态": [
            "是否激活",
            {"工作状态": ["前继节点", "后继节点", "负荷率", "并行任务数", "收件箱", "待处理任务集", "已处理任务集"]}
        ]}
    ]
}

edge_info = {"边":[
    {"ID": ["ID名", "ID编号"]},
    {"属性": ["方向", "通信时常", "最大承载量"]},
    {"功能": ["同步直接通信", "异步直接通信", "间接通信"]},
    {"状态": ["是否激活", "实时通信量"]}
]}

def formate_data(data):
    colors = ['#ec4646', "#663f3f", "#11698e", "#51c2d5", "#bbf1fa"]
    def deep_in(deep_data, deep_result, depth):
        deep_result["id"], deep_values = list(deep_data.items())[0]
        deep_result["color"] = colors[depth]
        deep_result['children'] = []
        for i, value in enumerate(deep_values):
            deep_result['children'].append({})
            if isinstance(value, dict):
                deep_in(value, deep_result['children'][i], depth+1)
            else:
                deep_result['children'][i]["id"] = value
                deep_result["children"][i]['color'] = colors[depth+1]
    result = {}
    deep_in(data, result, 0)
    return result
    
with open('data/nodes_info.json', 'w', encoding='utf-8') as json_file:
   json.dump(formate_data(node_info),  json_file)
   
   
# g6 tree graph
# import G6 from '@antv/g6';
# const data = {"id": "\u8282\u70b9", "color": "#ec4646", "children": [{"id": "ID", "color": "#663f3f", "children": [{"id": "ID\u540d", "color": "#11698e"}, {"id": "ID\u7f16\u53f7", "color": "#11698e"}]}, {"id": "\u5c5e\u6027", "color": "#663f3f", "children": [{"id": "\u804c\u7ea7", "color": "#11698e"}, {"id": "\u5904\u7406\u80fd\u529b", "color": "#11698e"}, {"id": "\u5904\u7406\u7528\u65f6", "color": "#11698e"}, {"id": "\u6982\u7387", "color": "#11698e"}]}, {"id": "\u529f\u80fd", "color": "#663f3f", "children": [{"id": "\u57fa\u672c\u529f\u80fd", "color": "#11698e", "children": [{"id": "\u4e1a\u52a1\u529f\u80fd", "color": "#51c2d5", "children": [{"id": "\u6027\u606f\u901a\u4fe1", "color": "#bbf1fa"}, {"id": "\u6d41\u7a0b\u5904\u7406", "color": "#bbf1fa"}, {"id": "\u77e5\u8bc6\u63a8\u7406", "color": "#bbf1fa"}]}, {"id": "\u7ba1\u7406\u529f\u80fd", "color": "#51c2d5", "children": [{"id": "\u4efb\u52a1\u8c03\u5ea6", "color": "#bbf1fa"}]}]}, {"id": "\u5b66\u4e60\u529f\u80fd", "color": "#11698e", "children": [{"id": "\u57fa\u672c\u529f\u80fd\u5b66\u4e60", "color": "#51c2d5"}, {"id": "\u5b66\u4e60\u65b0\u80fd\u529b", "color": "#51c2d5"}]}]}, {"id": "\u72b6\u6001", "color": "#663f3f", "children": [{"id": "\u662f\u5426\u6fc0\u6d3b", "color": "#11698e"}, {"id": "\u5de5\u4f5c\u72b6\u6001", "color": "#11698e", "children": [{"id": "\u524d\u7ee7\u8282\u70b9", "color": "#51c2d5"}, {"id": "\u540e\u7ee7\u8282\u70b9", "color": "#51c2d5"}, {"id": "\u8d1f\u8377\u7387", "color": "#51c2d5"}, {"id": "\u5e76\u884c\u4efb\u52a1\u6570", "color": "#51c2d5"}, {"id": "\u6536\u4ef6\u7bb1", "color": "#51c2d5"}, {"id": "\u5f85\u5904\u7406\u4efb\u52a1\u96c6", "color": "#51c2d5"}, {"id": "\u5df2\u5904\u7406\u4efb\u52a1\u96c6", "color": "#51c2d5"}]}]}]}

#     const container = document.getElementById('container');
#     const width = container.scrollWidth;
#     const height = container.scrollHeight || 500;
#     const graph = new G6.TreeGraph({
#       container: 'container',
#       width,
#       height,
#       linkCenter: true,
#       modes: {
#         default: [
#           {
#             type: 'collapse-expand',
#             onChange: function onChange(item, collapsed) {
#               const data = item.getModel();
#               data.collapsed = collapsed;
#               return true;
#             },
#           },
#           'drag-canvas',
#           'zoom-canvas',
#         ],
#       },
#       defaultNode: {
#         size: 20,
        
#         anchorPoints: [
#           [0, 0.5],
#           [1, 0.5],
#         ],
#       },
#       defaultEdge: {
#         color: "grey",
#         type: 'cubic-vertical',
#       },
#       layout: {
#         type: 'compactBox',
#         direction: 'TB',
#         getId: function getId(d) {
#           return d.id;
#         },
#         getHeight: function getHeight() {
#           return 16;
#         },
#         getWidth: function getWidth() {
#           return 16;
#         },
#         getVGap: function getVGap() {
#           return 55;
#         },
#         getHGap: function getHGap() {
#           return 30;
#         },
#       },
#     });

#     graph.node(function (node) {
#       let position = 'bottom';
#       let rotate = 0;
#       let textAlign = "center";
#       if (!node.children) {
#         textAlign = "start";
#         // position = 'bottom';
#         rotate = Math.PI / 2;
#       }
#       return {
#         label: node.id,
#         style: {stroke:node.color, lineWidth:10, fill:'white'},


#         labelCfg: {
#           position,
#           offset: 10,
          
#           style: {
#             rotate,
#             fontSize:20,
#             textAlign,
#           },
#         },
#       };
#     });

#     graph.data(data);
#     graph.render();
#     graph.fitView();

#     if (typeof window !== 'undefined')
#       window.onresize = () => {
#         if (!graph || graph.get('destroyed')) return;
#         if (!container || !container.scrollWidth || !container.scrollHeight) return;
#         graph.changeSize(container.scrollWidth, container.scrollHeight);
#       };
# setTimeout(()=>{graph.downloadImage()}, 1000)
